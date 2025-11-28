import time

timeout = time.clock_gettime(0)
actualtime = time.strftime("%b %d %Y")

print("Seconds since January 1, 1970:",
      "{:,.4f}".format(timeout), "or", "{:,.2e}".format(timeout),
      "in scientific notation")

print(actualtime)
