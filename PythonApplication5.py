import requests
import json
import string 

# 设定竞赛基本信息
contest_name = "第二届河北省大学生程序设计竞赛"  #名称
question_list = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022] # 题目编号列表



#请求问题信息
def get_question(question_num):
	question_url = 'http://140.143.222.61:8088//problem/'+str(question_num) #生成题目URL
	req = requests.get(url=question_url) # 发起请求
	question_str = req.text.encode('utf-8') # 编码
	question_JSON = json.loads(question_str) # str转JSON
	return question_JSON

#将JSON转换为Markdown
def question_md(question_num):
	global str_num
	question_md = ""
	question_JSON = get_question(question_num)
	if question_JSON['code'] == 0 :
		print(question_num,"题请求成功")
		question_info = question_JSON['data']
		question_title = "## 问题"+ chr(str_num)+ " " + str(question_info['id'])+" "+ question_info['title']+ "\n"
		question_limit = "时间限制："+ str(question_info['time_limit']) +"s 内存限制:" + str(question_info['memory_limit']) + "m\n"
		question_description = "### 描述\n" + question_info['description'] + "\n"
		question_input = "### 输入\n" + question_info['input'] + "\n"
		question_output = "### 输出\n" + question_info['output'] + "\n"
		question_sample_input = "### 样例输入\n" + "```\n" + question_info['sample_input'] + "\n```\n"
		question_sample_output = "### 样例输入\n" + "```\n" + question_info['sample_output'] + "\n```\n"
		question_hint = "### 提示\n" + question_info['hint'] + "\n"
		question_md="---\n" + question_title + question_limit + question_description + question_input + question_output + question_sample_input + question_sample_output + question_hint
	else:
		print(str(question_num),"题请求失败，状态码：",question_JSON['code'])
	return question_md



print("******************************")
print("*                            *")
print("*    NEUQ OJ试题文档生成     *")
print("*                            *")
print("******************************\n")

contest_md = ""
contest_md = contest_md+"# "+contest_name+"\n"
str_num = 65 # Asscii码计数，表示题号

for i in question_list:
	print ("开始爬取"+str(i)+"题")
	contest_md = contest_md + question_md(i)
	str_num = str_num + 1 # 题号增一

# 保存到文件
with open('question.md','w', encoding='utf-8') as f:
	f.write(contest_md)