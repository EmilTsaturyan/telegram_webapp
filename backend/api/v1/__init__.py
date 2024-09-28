from fastapi import APIRouter

from .adds import router as add_router
from .user import router as user_router
from .leaderboard import router as leaderboard_router
from .refrerals import router as refferals_router
from .task import router as task_router
from .farm import router as farm_router


router = APIRouter()
router.include_router(add_router, prefix='/add')
router.include_router(user_router, prefix='/users')
router.include_router(leaderboard_router, prefix='/leaderboard')
router.include_router(refferals_router, prefix='/referrals')
router.include_router(task_router, prefix='/task')
router.include_router(farm_router, prefix='/farm')
