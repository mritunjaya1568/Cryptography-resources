scoreboard players set @a localChecks 0

execute as @a[scores={search=1}] if block ~0 ~-1 ~1338 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~1 ~-1 ~1338 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~2 ~-1 ~1338 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~0 ~-1 ~1339 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~2 ~-1 ~1339 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~0 ~-1 ~1340 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~2 ~-1 ~1340 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~0 ~-1 ~1341 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~2 ~-1 ~1341 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~0 ~-1 ~1342 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~1 ~-1 ~1342 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~2 ~-1 ~1342 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~4 ~-1 ~1340 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~6 ~-1 ~1340 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~5 ~-1 ~1341 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~4 ~-1 ~1342 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~6 ~-1 ~1342 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~10 ~-1 ~1338 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~10 ~-1 ~1339 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~10 ~-1 ~1340 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~10 ~-1 ~1341 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~10 ~-1 ~1342 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~12 ~-1 ~1338 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~13 ~-1 ~1338 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~14 ~-1 ~1338 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~12 ~-1 ~1339 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~14 ~-1 ~1339 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~12 ~-1 ~1340 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~14 ~-1 ~1340 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~12 ~-1 ~1341 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~14 ~-1 ~1341 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~12 ~-1 ~1342 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~13 ~-1 ~1342 minecraft:white_concrete run scoreboard players add @a localChecks 1
execute as @a[scores={search=1}] if block ~14 ~-1 ~1342 minecraft:white_concrete run scoreboard players add @a localChecks 1

execute as @a[scores={search=1}] if score @s localChecks matches 34 run scoreboard players add @s checksPassed 1