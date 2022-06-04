            # SSD CODE USING FUNCTION.

firstpage = ("    1.Data Plans\n    2.Social Bundles\n    3.Balance Check\n    4.Roaming/Int'l\n    5.Borrow Credit/Recharge\n    6.Gift Data\n    7.Video Packs\n    8.Hot Deals\n    9.Chat Zigi")
# print(firstpage)
dataplan = ("    Buy Data Plans\n    1.Daily\n    2.Weekly\n    3.Monthly\n    4.2-3Months\n    5.Always on plans\n    6.Mifi Plans\n    7.Family Packs\n    8.Hot Deals\n    0.Back")
data_plan_daily= ("    1.N50 for 40MB\n   N100 for 100MB\n  3.N100 FOR 350MB(IG/TIKTOK/Youtube ONLY)\n   4.N200 for 200MB\n   5.N300 FOR 1GB\n   99.Next\n  0.Back")
data_plan_weekly =("   1.N200 for 1GB(IG/TIKTOK/Youtube ONLY)\n   2.N300 for 350MB\n   3.N500 for 1.5GB\n   4.N500 for 750MB(2-Week plan)\n   5.N1,500 for 6GB\n   6.N1000 for 2GB\n   99.Next\n   0.Back")
# print(dataplan)
socialbundle = ("   1.WhatsApp\n   2.Facebook\n   3.Instagram\n   4. TikTok\n   5.Ayooba\n   6.All social bundles\n   7.Youtube, Instagram, and Tiktok\n   8.Opera Mini & News\n   9.Social Mega bundle\n   99.Next\n   0.Back")
socialbundle_whats = ("   1.Daily @ N25\n   2.Weekly @ N50\n   3.Monthly @ N150\n   0.Back")
socialbundle_face = ("  Facebook\n.  1.Daily @ N25\n  2.Weekly @ N50\n  3.Monthly @ N150\n  0.Back")

balance_check = ("   Your data balance is -----")
roaming = ("   1.Roaming data bundles\n   2.Roaming Voice + Data Bundles\n   3.Free incoming roaming call\n   4.Int'l Caliing Bundle\n   5.Roaming Balance Check\n   0.Back")
borrowcredit = ("   1.Borrow Airtime\n   2.Borrow Data\n   3.Recharge\n   0.Back")
giftdata = ("   1.Transfer from Data Balance\n   2.Buy for a friend\n   3.Request from a friend\n   4.View Pending Request\n   0.Back\n   00.MainMenu")

videopacks = ("   Video Streaming Packs\n   1.Youtube Video Packs\n   2.StarTimes Video Packs\n3.1GB (YouTube Only)+ 500MB (Data access)\n   4.Showmax Mobile")
videopacks_you =("  1.1hour @N50\n  2.3hours @N130\n  3.500MB @ N50 (12am - 5am)\n  4.2GB Weekly @ N200 (11pm - 6am)\n  5.Check Balance")
videopacks_star =("  1.1Hour @N150\n  2.3Hours @N400\n  3.Check balance")


def ssd():
    pin = '*131#'
    print('Enter code here>>>')
    code = input('>>>')
    if code == pin:
        print(firstpage)
    else:
        print('enter valid code')
        ssd()
    # return code    
    ssd1()
    
    
def ssd1():
    print('Enter a number here>>>')
    code = input('>>>')
    if code == '1':
        print(dataplan)
        data()
    elif code == '2':
        print(socialbundle)
        social()
    elif code == '3':
        print(balance_check)
    elif code == '4':
        print(roaming)
        roam()
    elif code == '5':
        print(borrowcredit)
        borrow()
    elif code == '6':
        print(giftdata)
        gift()
    elif code == '7':
        print(videopacks)
        video()
    elif code == '0':
        print(firstpage)

def data():
    print('Enter number here>>>')
    enter = input('>>>')
    if enter == '1':
            print(data_plan_daily)
            enter = input('Enter number here>>>')
            if enter == '0':
                print(dataplan)
                print('Enter number here>>>')
                enter = input('>>>')
                if enter == '0':
                    print(firstpage)
                    ssd1()
    elif enter == '2':
            print(data_plan_weekly)
            enter = input('Enter number here>>>')
            if enter == '0':
                print(dataplan)
                print('Enter number here>>>')
                enter = input('>>>')
                if enter == '0':
                    print(firstpage)
                    ssd1()

def social():
    print('Enter number here>>>')
    enter = input('>>>')
    if enter == '1':
        print(socialbundle_whats)
        enter = input("Enter number here>>>")
        if enter == '0':
            print(socialbundle)
            print('Enter number here>>>')
            enter = input('>>>')
            if enter == '0':
                print(firstpage)
                ssd1()
    elif enter =='2':
        print(socialbundle_face)
        enter = input('Enter number here>>>')
        if enter == '0':
            print(socialbundle)
            print('Enter number here>>>')
            enter = input('>>>')
            if enter =='0':
                print(firstpage)
                ssd1()

def roam():
    print('Enter number here>>>')
    enter = input('>>>')
    if enter =='0':
        print(firstpage)
        ssd1()

def borrow():
    print('Enter number here>>>')
    enter = input('>>>')
    if enter =='0':
        print(firstpage)
        ssd1()

def gift():
    print('Enter number here>>>')
    enter = input('>>>')
    if enter =='0':
        print(firstpage)
        ssd1()

def video():
    print('Enter number here>>>')
    enter = input('>>>')
    if enter == '1':
        print(videopacks_you)
    elif enter == '2':
        print(videopacks_star)    

ssd()






