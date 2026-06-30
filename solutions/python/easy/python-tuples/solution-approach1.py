# ──────────────────────────────────────────────────
# Problem     Tuples 
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python
# Status      Accepted
# Submitted   2026-06-30, 05:04 p.m.
# ──────────────────────────────────────────────────

n = int(raw_input())
integer_list = map(int,raw_input().split())
t = tuple(integer_list)
print(hash(t))
