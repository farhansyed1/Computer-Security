# README
Labs for the course *DD2395 Computer Security* at KTH.

In this repository, we have resources for the following:
- [Lab O (buffer-overflow)](buffer-overflow): Develop buffer-overflow attacks targeting vulnerable applications.
- [Denial of Service](dos): Develop a filter for preventing Denial-of-Service attack on a simple compression algorithm.
- [(In)secure hash function](hash): Develop a function that given a plaintext, find another plaintext whose hashes collides.
- [Malware](malware): Develop a simple antivirus program.
- [Side channels](side-channel): Develop a side-channel attack against an encryption algorithm.

These assignments uses an automatic grading system.
To submit your solutions to the grading system, simply make a commit and push.
```bash
git add [my solution file]
git commit -m"Adds my solution to foobar"
git push
```
Feedback from the grading system will appear as a comment on your commit on GitS.

The locations of the solutions files for the exercises and lab O are
*hardcoded*.  If they are moved, the automatic grading system will not be able
to test your solutions.

Solution files:
- `buffer-overflow/task1/solution1.txt`
- `buffer-overflow/task2/solution2.txt`
- `buffer-overflow/task3/solution3.py`
- `buffer-overflow/task4/solution4.py`
- `buffer-overflow/task5/solution5.py`
- `buffer-overflow/task6/solution6.py`
- `buffer-overflow/task7/solution7.py`
- `dos/filter.py`
- `hash/collision.py`
- `malware/antivirus.py`
- `side-channel/attack.py`
