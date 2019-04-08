from fabric import task

def test():
	local("nosetests -v")

	
def commit():
	message = raw_input("Enter a git commit message: ")
	local("git add . && git commit -am '{}'".format(message))

	
def push():
	local("git push origin master")

@task
def prepare(ctx):
	test()
	commit()
	push()