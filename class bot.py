import datetime, pyautogui as p, webbrowser, time

day = datetime.datetime.now().strftime("%A")
hour = datetime.datetime.now().strftime("%H:%M")

def zoom_meeting(subject_id:str, password:str):
    """func which takes subject id and password as an argument and, basically zoom automation"""
    time.sleep(10)
    p.click(530, 281)
    time.sleep(2)
    p.click(651, 323)
    time.sleep(1)
    p.typewrite(subject_id)
    p.press('enter')
    time.sleep(5)
    p.typewrite(password)
    p.press('enter')

def google_meet(classlink:str):
    """
    Google meet automation.
    """
    wb = webbrowser.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    wb.open_new(classlink)


if __name__ == "__main__":

    # monday schedule
    if day == "Monday":
        if hour == "9:00" or hour == "9:01" or hour == "9:02" or hour == "9:03" or hour == "9:04" or hour == "9:05":
            # PHY211
            zoom_meeting("PHY211", "PHY211")

        elif hour == "11:20" or hour == "11:21" or hour == "11:22" or hour == "11:23" or hour == "11:24" or hour == "11:25":
            # MTH211
            google_meet("MTH211")

        elif hour == "12:30" or hour == "12:31" or hour == "12:32" or hour == "12:33" or hour == "12:34" or hour == "12:35":
            # BIO211
            zoom_meeting("BIO211", "BIO211")

        elif hour == "3:40" or hour == "3:41" or hour == "3:42" or hour == "3:43" or hour == "3:44" or hour == "3:45":
            # CHM211
            zoom_meeting("CHM211", "CHM211")

        else:
            print("NO class right now!")


    # tuesday schedule
    elif day == "Tuesday":
        if hour == "10:10" or hour == "10:11" or hour == "10:12" or hour == "10:13" or hour == "10:14" or hour == "10:15":
            # BIO211
            google_meet("BIO211")

        elif hour == "12:30" or hour == "12:31" or hour == "12:32" or hour == "12:33" or hour == "12:34" or hour == "12:35":
            # CHM211
            zoom_meeting("CHM211", "CHM211")

        elif hour == "3:40" or hour == "3:41" or hour == "3:42" or hour == "3:43" or hour == "3:44" or hour == "3:45":
            # PHY211
            zoom_meeting("PHY211", "PHY211")

        else:
            print("NO class right now!")


    # wednesday schedule
    elif day == "Wednesday":
        if hour == "9:00" or hour == "9:01" or hour == "9:02" or hour == "9:03" or hour == "9:04" or hour == "9:05":
            # CHM211
            google_meet("CHM211")

        elif hour == "2:30" or hour == "2:31" or hour == "2:32" or hour == "2:33" or hour == "2:34" or hour == "2:35":
            # BIO213
            google_meet("BIO213")

        else:
            print("NO class right now!")


    # thursday schedule
    elif day == "Thursday":
        if hour == "9:00" or hour == "9:01" or hour == "9:02" or hour == "9:03" or hour == "9:04" or hour == "9:05":
            # PHY211
            google_meet("PHY211")   

        elif hour == "11:20" or hour == "11:21" or hour == "11:22" or hour == "11:23" or hour == "11:24" or hour == "11:25":
            # MTH211
            zoom_meeting("MTH211", "MTH211")

        elif hour == "2:30" or hour == "2:31" or hour == "2:32" or hour == "2:33" or hour == "2:34" or hour == "2:35":
            # BIO213
            zoom_meeting("BIO213", "BIO213")

        else:
            print("NO class right now!")


    # friday schedule
    elif day == "Friday":
        if hour == "9:00" or hour == "9:01" or hour == "9:02" or hour == "9:03" or hour == "9:04" or hour == "9:05":
            # BIO213
            zoom_meeting("BIO213", "BIO213")

        elif hour == "11:20" or hour == "11:21" or hour == "11:22" or hour == "11:23" or hour == "11:24" or hour == "11:25":
            # BIO211
            zoom_meeting("BIO211", "BIO211")

        elif hour == "2:30" or hour == "2:31" or hour == "2:32" or hour == "2:33" or hour == "2:34" or hour == "2:35":
            # MTH211
            zoom_meeting("MTH211", "MTH211")

        else:
            print("NO class right now!")


    else:
        print("Holiday! Enjoy.")