from invoke import task

@task
def myTest(ctx, in_file='Simon', out_file='Simon'):
    print("Hello")    
    print("In: " + in_file)
    print("Out: " + out_file)
    ctx.run("dir")

@task
def myCircumference(ctx, diameter=10.5):
    print("Circumference = ", 3.141 * diameter)



