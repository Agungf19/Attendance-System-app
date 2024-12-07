import redis

# Connect to Redis Client
hostname = 'redis-14983.c245.us-east-1-3.ec2.redns.redis-cloud.com'
portnumber = 14983
password = 'K1Qnj8CVull2u15iDsFUIXial0EtJves'

r = redis.StrictRedis(host=hostname,
                      port=portnumber,
                      password=password)

# Simulated Logs
with open('simulated_logs.txt', 'r') as f:
    logs_text = f.read()

encoded_logs = logs_text.split('\n')

# Push into Redis database
r.lpush('attendance:logs', *encoded_logs)