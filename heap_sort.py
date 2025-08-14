def heapify(arr, n, i):
    """i를 루트로 하는 서브트리를 최대 힙으로 만드는 함수"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """Heap Sort 알고리즘"""
    n = len(arr)

    # 최대 힙 생성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 원소 하나씩 꺼내 힙 재구성
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# -------------------------
# 실행
# -------------------------
print("\n=== Heap Sort 실행 ===")
heap_sort(data_list)
print("정렬된 데이터:", data_list)