import progressbar, time, sys

def up():
    # My terminal breaks if we don't flush after the escape-code
    sys.stdout.write('\x1b[1A')
    sys.stdout.flush()

def down():
    # I could use '\x1b[1B' here, but newline is faster and easier
    sys.stdout.write('\n')
    sys.stdout.flush()

# Total bar is at the bottom. Move down to draw it
down()
total = progressbar.ProgressBar(maxval=50)
total.start()

for i in range(1,51):
    # Move back up to prepare for sub-bar
    up()

    # I make a new sub-bar for every iteration, thinking it could be things
    # like "File progress", with total being total file progress.
    sub = progressbar.ProgressBar(maxval=50)
    sub.start()
    for y in range(51):
        sub.update(y)
        time.sleep(0.005)
    sub.finish()

    # Update total - The sub-bar printed a newline on finish, so we already
    # have focus on it
    total.update(i)
total.finish()