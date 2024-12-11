# Advent of Code 2024

Second year of [Advent of Code](https://adventofcode.com/)!

🐍 Python 🐍

❌🤖 No LLMs allowed 🤖❌

# Stats

### Official stats:

| Day | Part 1 Time | Part 1 Rank | Part 1 Score | Part 2 Time | Part 2 Rank | Part 2 Score |
| --- | ----------- | ----------- | ------------ | ----------- | ----------- | ------------ |
| 11  | 00:06:22    | 971         | 0            | 01:46:19    | 7276        | 0            |
| 10  | 00:14:21    | 1881        | 0            | 00:15:50    | 1395        | 0            |
| 9   | 00:46:06    | 5838        | 0            | 00:59:40    | 2521        | 0            |
| 8   | 01:02:20    | 7464        | 0            | 01:20:01    | 7107        | 0            |
| 7   | >24h        | 51121       | 0            | >24h        | 48263       | 0            |
| 6   | 00:33:36    | 6502        | 0            | 00:44:30    | 2865        | 0            |
| 5   | 00:19:40    | 3977        | 0            | 00:31:08    | 3190        | 0            |
| 4   | 00:46:33    | 8858        | 0            | 00:52:56    | 6798        | 0            |
| 3   | 00:12:01    | 5146        | 0            | 00:15:24    | 2414        | 0            |
| 2   | 00:08:15    | 1762        | 0            | 01:21:14    | 10432       | 0            |
| 1   | 01:04:33    | 10474       | 0            | 01:10:38    | 9930        | 0            |

<br><br>

### Personal times:

(Times are starting from when I actually opened each part of the puzzle)

| Day | Started  | Part 1 Time to Solve | Part 2 Time to Solve |
| --- | -------- | -------------------- | -------------------- |
| 11  | 00:00:00 | 00:06:22             | 01:39:57             |
| 10  | 00:00:00 | 00:14:21             | 00:01:29             |
| 9   | 00:00:00 | 00:46:06             | 00:13:34             |
| 8   | 00:00:00 | 01:02:20             | 00:17:41             |
| 7   | 25:33:46 | 00:07:38             | 00:08:29             |
| 6   | 00:00:00 | 00:33:36             | 00:10:54             |
| 5   | 00:10:02 | 00:09:38             | 00:11:28             |
| 4   | 00:00:00 | 00:46:33             | 00:06:23             |
| 3   | 00:00:00 | 00:12:01             | 00:03:23             |
| 2   | 00:00:00 | 00:08:15             | 01:12:59             |
| 1   | 00:57:31 | 00:07:02             | 00:06:05             |

### Personal notes:

## ⚠️ **Warning! Spoilers ahead** ⚠️

<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>

| Day | Personal Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 11  | From the highest of highs to the lowest of lows... for part 2 I thought of some variant of the pebble bucketing solution (ie just counting the number of pebbles with each engraving) many times, but kept getting stuck on the incorrect belief that I would still have to track the number of blinks that each new pebble has seen. <br><br>Eventually chanced upon a sort of halfway solution where I consolidate the pebbles if there are a lot of them, but it's somewhat slow (48s with pypy). But hey if it works it works! (Also if I'd thought of it right after part 1, it might have been one of the fastest to implement) |
| 10  | Feeling pretty slick today, but it seems like this was an easier problem for everybody. Lost about a minute on the second part due to getting used to nvim again (so nice to have an editor that doesn't corrupt edit history... looking at you VSCode...)                                                                                                                                                                                                                                                                                                                                                                            |
| 9   | Bit of a rollercoaster today - <br> - 📉 Started part 1 by misreading it as what turned out to be the part 2 problem <br> - 📈 After 20 minutes, realizing that IDs can be longer than 1 character in width <br> - 📈 Reading part 2, realizing that I'd already solved it <br> - 📉 Realizing that my solution had the same IDs issue <br> - 📈 Fixing the issue relatively quickly <br><br> All in all kind of a clown day but not awful.                                                                                                                                                                                           |
| 8   | Didn't do day 7 yet - made some pretty silly mistakes and didn't read the question properly the first time (turns out "in line" is actually a meaningful term for solving the problem, not just exposition).                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 7   | Did this right after day 8 and it felt considerably easier. Might have gotten lucky though                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 6   | Thought for a second that my brute force part 2 solution wouldn't complete in time -- again, pypy to the rescue. Slow start because I forgot that a path can overlap itself.<br><br> Also starting to notice some differences in my approach to implementing solutions this year, namely that I'm not as concerned with writing good-looking code and it's counterintuitively easier to read as a result (at least to me) and faster to write (and therefore more fun)                                                                                                                                                                |
| 5   | Brute force + pypy is your friend                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 4   | Lil off by 1s everywhere in pt 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 3   | Relearning regex in pt 1 pays off!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 2   | Clowned on pt 2 by checking every case (and messing that up) instead of brute forcing it; also lost ~30s to brief site outage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 1   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
