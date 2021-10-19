import redis

r = redis.Redis('localhost', 6379, db=1)  # connecting to the redis
redis_m = r.get('ticker_screaner_1m')  # get the ticker dict from server
