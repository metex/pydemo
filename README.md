seq -f "Line %05g" 10000 > sample.txt
curl -F "file=@sample.txt" -F "resumable=2" http://httpbin.org/post
curl -F "file=@sample.txt" -F "resumable=2" https://hookb.in/r1L3ZdxyzLcQnP1o2lqb
curl -X POST -H "Content-Type: application/json" -d '{"name": "John"}' https://hookb.in/r1L3ZdxyzLcQnP1o2lqb
curl --trace trace.txt -F "file=@sample.txt" -F "resumable=2" http://httpbin.org/post