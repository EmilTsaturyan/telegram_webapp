from fastapi import APIRouter, Depends

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Wallet, User
from db import database
from schemas import LeaderboardResponse


router = APIRouter(tags=['Leaderboard'])
from cache import cache_manager



@router.get('/', response_model=list[LeaderboardResponse])
@cache_manager.cache_response(key='leaderboard', ttl=600)
async def get_leaderboard(session: AsyncSession = Depends(database.get_async_session)):
    result = await session.execute(
        select(Wallet, User)
        .join(Wallet.user)  # Join Wallet with its related User
        .order_by(Wallet.coins.desc())
        .limit(100)
    )
    
    # Extract the Wallet and User data
    wallets_with_users = result.all()

    # Format the result to include username or first_name along with wallet data
    leaderboard = [
        {
            "id": wallet.id,
            "coins": wallet.coins,
            "username": user.username or user.first_name,  # Use username, or first_name if username is not available
        }
        for wallet, user in wallets_with_users
    ]
    return leaderboard