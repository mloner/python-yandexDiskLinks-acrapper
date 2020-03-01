import string, random, sys, _thread, requests

if len(sys.argv) < 2 or len(sys.argv) > 3:
    sys.exit("Number of arguments must be [1..2])")

THREAD_AMOUNT = int(sys.argv[1])

INVALID = [404] #codes of wrong data
linksInThread = [] #target amount of pics by every thread
currentLinksInThread = [] #current amount of pics by every thread
done = False #flag of end of program
goodLinks = []

if len(sys.argv) > 2: #if have threads count
    count = int(sys.argv[2]) // int(sys.argv[1])

    for i in range(int(sys.argv[1])):
        currentLinksInThread.append(0)

    for i in range(int(sys.argv[1])):
        linksInThread.append(count)

    if int(sys.argv[2]) % int(sys.argv[1]) != 0:
        last = int(sys.argv[2]) - int(sys.argv[1]) * count
        linksInThread[int(sys.argv[1]) - 1] += last

def scrape_links(thread):
    global done
    while True:
        if len(sys.argv) > 2 and int(currentLinksInThread[int(thread)-1]) >= int(linksInThread[int(thread)-1]):
            print("thread " + thread + " done")
            pass
            if currentLinksInThread == linksInThread:
                print("All threads are done")
                done = True
            sys.exit()
        try:
            url = 'https://yadi.sk/d/'
            adress = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(14))
            #print(adress)
            url += adress
            response = requests.get(url)
            if response.status_code == 200: #adress exists
                print(url)
                goodLinks.append(url + '\n')
                currentLinksInThread[int(thread) - 1] += 1
        except Exception:
            pass
for thread in range(1, THREAD_AMOUNT + 1):
    thread = str(thread)
    try:
        _thread.start_new_thread(scrape_links, (thread,))
    except:
        print('Error starting thread ' + thread)
print('Succesfully started ' + thread + ' threads.')
if __name__ == '__main__':
    while not done:
        pass
    file = open('links.txt', 'w')
    for link in goodLinks:
        file.write(link)
    file.close()
    print("Script is done")
