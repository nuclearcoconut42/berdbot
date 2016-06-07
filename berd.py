import sopel.module
import random

@sopel.module.commands('berd')
def berd(bot, trigger):
    berds = [".>.", ".<.", "berd", ":>", "<:", "'v'", "tweet", "chirp"]
    berdEmotes = ["berds", "tweets at", "chirps at"]
    if(random.randint(0,1)):
        bot.say(random.choice(berds))
    else:
        bot.action(random.choice(berdEmotes) + ' ' + trigger.nick)

@sopel.module.commands('bots')
def bots(bot, trigger):
    bot.say('Reporting in! [Python] [Is stupid]')
