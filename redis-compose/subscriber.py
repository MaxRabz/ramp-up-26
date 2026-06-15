import redis

r = redis.Redis(host="redis", port=6379, decode_responses=True)

CHANNEL = "messages"

pubsub = r.pubsub()
pubsub.subscribe(CHANNEL)

print(f"Listening on channel: {CHANNEL}")

for message in pubsub.listen():
    if message["type"] == "message":
        print("Received:", message["data"])