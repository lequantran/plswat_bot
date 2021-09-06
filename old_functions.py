@client.command()
async def uwu(ctx, *args):
    await ctx.message.delete()
    if len(args) == 1:
        if int(args[0]) < 4 and int(args[0]) > -1:
            response = uwu_kill[int(args[0]) - 1]      
            await ctx.send(response) 
        else:
            await ctx.send('Number **{}** invalid. Please use .uwu for help!'.format(args[0]))
    else:
        await ctx.send('How to use the command:\n**.uwu (number)**\n with number = {1,2,3}')  
