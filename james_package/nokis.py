
print("""List of menu function
        1.phone book
        2.messages
        3.chat
        4.call register
        5.tones
        6.settings
        7.call divert
        8.games
        9.calculator
        10.reminder
        11.clock
        12.profiles
        13.Sim services**3
        """)
menu_number = int(input("Enter menu_number: "))
if menu_number == 1:
    print("""phone book
           1.Search
           2.Service Nos.**1
           3.Add name
           4.Erase
           5.Edit
           6.Assign tone
           7.Send b'card
           8.option
           9.speed dials
           10.Voice tags

         """)

    menu_number_1 = int(input("Enter menu_number 1: "))

    if menu_number_1 == 8:
        print("""option
              1.Type of view
              2.Memory status
              
              """)








if menu_number == 2:
    print("""Messages
           1.Write messages
           2.inbox
           3.Outbox
           4.Picture messages
           5.Templates
           6.Smileys
           7.Messages settings
           8.info service
           9.Voice mailbox number
           10.Service command editor
           """)
    menu_number_2 = int(input("Enter menu_number 2: "))

    if menu_number_2 == 7:
        print("""Messages settings
            1.set 1**2
            2.common**3
            """)
        menu_number_7 = int(input("Enter menu_number 7: "))
        if menu_number_7 == 1:
            print("""set 1**2
                 1.Messages centre number
                 2.Messages sent as
                 3.Messages validity
                  """)
        if menu_number_7 == 2:
            print(""" Common**3
                       1.Delivery reports
                       2.Reply via same centre
                       3.Character support
                """)

if menu_number == 3:
    print("Chat")

if menu_number == 4:
    print(""" Call register
            1.Missed calls
            2.Received calls
            3.Dialled numbers
            4.Erase recent call lists
            5.Show call duration
            6.show costs
            7.Call cost settings
            8.prepaid
            """)
    menu_number_4 = int(input("Enter the menu number 4"))


    if menu_number_4 == 6:
        print("""Show call cost
               1.Last call cost
               2.All calls' cost
               3.Clear counters
               """)
    if menu_number_4 == 7:
        print("""Call cost settings
               1.Call cost limit
               2.Show costs in
              """)
if menu_number == 5:
    print("""Tones
            1.Ringing tone
            2.Ringing volume
            3.Incoming  call alert
            4.Composer
            5.Message alert tone
            6.Keypad tones
            7.Warning and game tones
            8.Vibrating alert
            9.Screen saver
             """)
if menu_number == 6:
    print("""Settings
            1.Call settings
            2.Phone settings
            3.Security settings
            4.Restore factory
            """)
    menu_number_6 = int(input("Enter menu number 6: "))
    if menu_number_6 == 1:
        print("""Calling settings
            1.Automatic redial
            2.Speed dialling
            3.Call waiting option
            4.Own number sending
            5.Phone line in use
            6.Automatic answer**1
            """)
    if menu_number_6 == 2:
        print("""Phone settings
             1.Language
             2.Cell info display
             3.Welcome note
             4.Network selection
             5.lights**2
             6.Confirm SIM service actions

             """)
    if menu_number_6 == 3:
        print("""Security settings
              1.PIN code request
              2.Call barring service
              3.Fixed dialling
              4.Closed user group
              5.Phone security
              6.Change access codes
        """)
if menu_number == 11:
    print("""Clock
            1.Alarm clock
            2.Clock settings
            3.Date settings
            4.Stopwatch
            5.Countdown timer
            6 Auto update of date and  time
              """)
