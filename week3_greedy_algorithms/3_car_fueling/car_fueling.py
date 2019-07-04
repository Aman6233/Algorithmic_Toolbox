# python3
import sys


def compute_min_refills(distance, tank, stops):
	stops.insert(0, 0)
	stops.append(distance)
	numfills = 0
	currentfill = 0
	while stops[currentfill]<=stops[-2]:
		lastfill = currentfill
		while stops[currentfill]<=stops[-2] and stops[currentfill+1]-stops[lastfill]<=tank:
			currentfill += 1
		if currentfill == lastfill:
			return -1
		if stops[currentfill]<=stops[-2]:
			numfills += 1

	return numfills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
