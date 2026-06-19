# AsyncAPI protocol usage — full corpus (document-level)

Protocols declared anywhere in each spec (servers' `protocol` + binding keys), across the WHOLE corpus — not just the request/reply slice. `specs / repos` per version.

- 3.x: 4151 parsed specs, 1397 declare a protocol (902 repos).
- 2.x: 2701 parsed specs, 1627 declare a protocol (984 repos).

| Protocol | 3.x (specs / repos) | 2.x (specs / repos) |
| -------- | ------------------: | ------------------: |
| kafka | 393 / 193 | 472 / 201 |
| ws | 229 / 203 | 459 / 250 |
| mqtt | 219 / 116 | 281 / 127 |
| amqp | 173 / 107 | 228 / 106 |
| wss | 218 / 173 | 140 / 112 |
| http | 179 / 110 | 145 / 81 |
| sqs | 65 / 34 | 11 / 9 |
| solace | 15 / 1 | 58 / 13 |
| nats | 42 / 29 | 31 / 27 |
| sns | 34 / 30 | 23 / 9 |
| ibmmq | 9 / 9 | 44 / 7 |
| redis | 20 / 14 | 23 / 19 |
| googlepubsub | 19 / 10 | 13 / 5 |
| anypointmq | 7 / 1 | 24 / 5 |
| jms | 15 / 8 | 7 / 5 |
| pulsar | 7 / 5 | 13 / 5 |
| stomp | 7 / 6 | 12 / 9 |
| mqtt5 | 10 / 2 | 5 / 3 |
| amqp1 | 3 / 2 | 7 / 4 |
| mercure | 5 / 8 | 5 / 2 |
