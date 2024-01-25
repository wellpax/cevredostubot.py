import discord
from discord.ext import commands




intents=discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)
intents.message_content=True

@bot.event
async def on_ready():
    print(f'{bot.user}olarak giriş yaptık')

@bot.command(name='kirlilik')
async def kirlilik(ctx):
    
    tavsiyeler = [
        "Atıklarınızı geri dönüşüme kazandırın.",
        "Enerji tasarrufu sağlamak için bilinçli tüketim yapın.",
        "Plastik kullanımını minimumda tutun ve plastik atıkları geri dönüşüme gönderin.",
        "Su tasarrufu yapmak için bilinçli su kullanımı sağlayın.",
        "Doğaya zarar vermemek için yeşil enerji kaynaklarına destek verin.",
        "Toplu taşıma veya bisiklet kullanarak karbon ayak izinizi azaltın.",
        "Atık miktarını azaltmak için sıfır atık prensiplerini benimseyin.",
        "Doğayı korumak için ağaç dikimine katılın veya bağışta bulunun."
    ]

    
    await ctx.send("Çevre kirliliğini engellemek için aşağıdaki önerilere göz atabilirsiniz:\n\n" + "\n".join(tavsiyeler))


@bot.command(name='resim')
async def resim(ctx):
 
    resim_url = 'https://eco.euwomanbg.com/wp-content/uploads/2020/02/publ-min-1-400x213.jpg'

  
    await ctx.send(f"İşte resminiz:\n{resim_url}")

bot.run('TOKEN')
