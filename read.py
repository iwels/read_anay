data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

print('讀取完成，共有', len(data), '筆資料')

sum_length = 0
for d in data:
	sum_length = sum_length + len(d)

print('每一筆的平均長度為', sum_length/len(data), '個字')