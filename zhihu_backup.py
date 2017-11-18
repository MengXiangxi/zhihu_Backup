from zhihu_oauth import ZhihuClient, ActType
from zhihu_oauth.exception import NeedCaptchaException
import codecs
import time

client = ZhihuClient()
client.load_token('token.pkl')
me = client.me()

print('name', me.name)

i = 0

l1 = '<meta name="referrer" content="no-referrer" />'
l2 = '<meta charset="utf-8" />'

for act in me.activities:
    if act.type == ActType.CREATE_ANSWER:
        #act.target.save()
        i += 1
        filename = 'Answer'+str(i)+'.html'
        with codecs.open(filename,'w','utf-8') as file:
            file.write(l1+'\n')
            file.write(l2+'\n')
            file.write('<h1> '+act.target.question.title+' </h1>\n')
            file.write(act.target.content)
            ans_time = time.ctime(act.target.created_time)
            file.write('\n<p>Time: '+str(ans_time)+'</p>\n')
            file.write('<p>Upvotes: '+str(act.target.voteup_count)+'</p>\n')
