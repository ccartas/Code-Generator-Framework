import json
import os
import io
import inspect
import fileinput
from string import Template

os.chdir(os.path.abspath(__file__).split('app.py')[0])
config = json.loads(open('config/config.json').read())


language = config['language']
if language == 'java':
	type = config['type']
	package = config['package'].replace(".","/")
	fileNames = config['name'].split(",")
	

	if type == 'class':
		attributes = config['attributes']
		for x in fileNames:
			os.makedirs(os.path.dirname("output/"+package+"/"),exist_ok=True)
			file = open("output/"+package+"/"+x+".java", "w+")
			filein = open('templates/javaClass.txt')
			source = Template( filein.read() )
			attrs = []
			constructor = []
			getters= []
			setters= []
			for key, value in attributes.items():
				attrs.append(value + " " + key)
				getters.append("\npublic "+ value +" get"+key.upper()+"{\n"+"return this."+key+";"+"\n\t}")
				setters.append("\npublic void "+"set"+key.upper()+"("+value+ " "+key+"){\n"+"this."+key+"="+key+";"+"\n\t}")

			constructor.append("\npublic "+x+"(){"+"\n\t}")

			d={'package': package.replace("/","."), 'name':x, 'attrs': '\n\t'.join(attrs),'constructor':'\n\t'.join(constructor),'getters':'\n\t'.join(getters),'setters':'\n\t'.join(setters)}
			result = source.substitute(d)
			file.write(result)
			file.close()
			filein.close()
	if type == 'interface':
		methods = config['methods']
		for x in fileNames:
			os.makedirs(os.path.dirname("output/"+package+"/"),exist_ok=True)
			file = open("output/"+package+"/"+x+".java", "w+")
			filein = open('templates/javaInterface.txt')
			source = Template( filein.read() )
			meths = []
			for key,value in methods.items():
				meths.append("public " + value + " "+key+"();")
			d={'package':package.replace("/","."),"name":x, 'methods':'\n\t'.join(meths)}
			result = source.substitute(d)
			file.write(result)
			file.close()
			filein.close()

if language == 'javascript':
	modules = config['modules'].split(",")
	appName = config['appName']
	os.makedirs(os.path.dirname("output/js/"+appName+"/"),exist_ok=True)
	file = open("output/js/"+appName+"/app.js","w+")
	filein = open('templates/javascriptModule.txt')
	source = Template( filein.read() )
	moduleNames = []
	for x in modules:
		moduleNames.append(x+"Module")
	d = {'appName':appName, 'dependencies':moduleNames}
	result = source.substitute(d)
	file.write(result)
	file.close()
	filein.close()

	for module in modules:
		
		#creating each module folder and module javascript files
		os.makedirs(os.path.dirname("output/js/"+appName+"/"+module+"/"),exist_ok=True)
		file = open("output/js/"+appName+"/"+module+"/app-"+module+".js","w+")
		filein = open("templates/javascriptModule.txt")
		source = Template( filein.read() )
		d={'appName':"'"+module+"Module'", 'dependencies': "[]"}
		result = source.substitute(d)
		file.write(result)
		file.close()
		filein.close()

		#creating each service file
		os.makedirs(os.path.dirname("output/js/"+appName+"/"+module+"/service/"), exist_ok=True)
		file = open("output/js/"+appName+"/"+module+"/service/"+module+"Service.js","w+")
		filein = open("templates/javascriptService.txt")
		source = Template ( filein.read() )
		d={'moduleName':"'"+module+"Module'", 'serviceName':"'"+module+"Service'", 'service': module+"Service", 'inject':'$inject'}
		result = source.substitute(d)
		file.write(result)
		file.close()
		filein.close()	

		#creating each controller file and including the service as dependency
		os.makedirs(os.path.dirname("output/js/"+appName+"/"+module+"/controller/"), exist_ok=True)
		file = open("output/js/"+appName+"/"+module+"/controller/"+module+"Controller.js","w+")
		filein = open("templates/javascriptController.txt")
		source = Template ( filein.read() )
		d = {'moduleName':"'"+module+"Module'", 'controllerName':"'"+module+"Controller'",'controller': module+"Controller", 'inject':"$inject", 'serviceName':"'"+module+"Service'",'service':module+"Service"}
		result = source.substitute(d)
		file.write(result)
		file.close()
		filein.close()











		