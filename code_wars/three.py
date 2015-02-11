def f(x):
    return {
      '1': 30,
      '2': 5*15,
      '3': 5*15,
      '4': 4*15,
      '5': 5*15,
      '6': 6*15,
      '7': 3*15,
      '8': 7*15,
      '9': 6*15,
      '0': 6*15,
      }.get(x,0)

for i in range(0, int(input())):
    time = list(input())
    nums = []
    for n in range(0,len(time)):
        nums.append(time[n])
    nums.remove(":")
    amps = 20
    for j in range(0, len(nums)):
        amps += f(nums[j])
    print(str(amps) + ' milliamps')

