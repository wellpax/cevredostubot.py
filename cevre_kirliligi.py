import discord
from discord.ext import commands
import time



intents=discord.Intents.default()

intents.message_content=True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user}olarak giriş yaptık')

@bot.command()
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


@bot.command()
async def video(ctx):
 
    video_url = 'https://www.youtube.com/watch?v=vpc-RwXwtH8'

  
    await ctx.send(f"İşte videonuz:\n{video_url}")



@bot.command()
async def resim(ctx):
    with open(r'resimler\cevrekirlilikresim\cevrekirlilikdcbot.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    time.sleep(1)
    await ctx.send(f'Hep birlikte tercih ve alışkanlıklarımızı değiştirerek çevre kirliliği sorununu çözmeye çalışalım ve dünyamızı temiz tutalım.')


bot.run('TOKEN')
