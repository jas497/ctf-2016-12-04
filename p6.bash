base=https://ctf.brennan.io/linkedlist/
frob=${base}3506824557
while [ 1 ]; do
	page=$(curl -s $frob)
	echo $page
	num=$(echo $page | grep -Po ": \K(.*?)$")
	frob=$base$num
done
