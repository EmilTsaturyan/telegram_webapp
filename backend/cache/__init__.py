from .cache import SimpleCache, CacheManager

# Create a simple in-memory cache
cache = SimpleCache()

# Create a CacheManager instance with the SimpleCache
cache_manager = CacheManager(cache=cache)