def reverse(st):
    for line in st.split('\n'):
        return (' '.join(line.split()[::-1]))