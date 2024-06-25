from line_profiler import LineProfiler

def rock(rk):
    print(rk)

rk = "Hello world"
profile = LineProfiler(rock(rk))

print(profile.print_stats())