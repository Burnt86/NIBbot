
message = 'https://old.reddit.com/thisisalink/test/http://old.reddit.com/https://old.reddit.com'
# message = 'https://old.reddit.com/thisisalink/test/https://old.reddit.com'

newcontent = message.lower().replace('https://old.reddit.com', 'https://www.reddit.com')

newcontent = newcontent.lower().replace('http://old.reddit.com', 'https://www.reddit.com')


print(newcontent)