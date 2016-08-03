import sopel.module
import random

@sopel.module.commands('berd')
def berd(bot, trigger):
    if trigger.group(2) is None:
        args = []
    else:
        args = trigger.group(2).strip().split(' ')
    berds = [".>.", ".<.", "berd", ":>", "<:", "'v'", "tweet", "chirp"]
    berdEmotes = ["berds", "tweets at", "chirps at"]
    if args is None:
        if(random.randint(0,1)):
            bot.say(random.choice(berds))
        else:
            bot.action(random.choice(berdEmotes) + ' ' + trigger.nick)
    else:
        if(random.randint(0,1)):
            bot.say(args[0] + ": " + random.choice(berds))
        else:
            bot.action(random.choice(berdEmotes) + ' ' + args[0])

@sopel.module.commands('bots')
def bots(bot, trigger):
    bot.say('Reporting in! [Python] [Is stupid]')
