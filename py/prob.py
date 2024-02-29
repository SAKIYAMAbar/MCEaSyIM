def from_file(filename,model):
    data = []  # セットごとのデータを格納するリスト
    max = 0 # ノードの最大値を保持する変数
    with open(filename, "r") as f: # ファイルを開く
        for line in f: # ファイルの各行に対して
            elements = line.split()  # 空白で分割して要素を取得する
            if len(elements) == 2: # 要素が2つであれば
                set_data = (int(elements[0]), int(elements[1])) # 要素を整数に変換してタプルにする
                data.append(set_data) # リストにタプルを追加する
                if max <= int(elements[0]): # ノードの最大値を更新するか判定する
                  max = int(elements[0]) # ノードの最大値を更新する
                if max <= int(elements[1]): # ノードの最大値を更新するか判定する
                  max = int(elements[1]) # ノードの最大値を更新する
    n = max + 1 # ノード数を求める
    nodes = {} # ノードの辞書を作る
    edges_M = {} # カスケードAのエッジの辞書を作る
    edges_C = {} # カスケードBのエッジの辞書を作る
    for i in range(n): # すべてのノードに対して
        nodes[i] = i # ノードの値をノード自身にする
    degree = {}
    for u in range(n):
        degree[u] = 0
    for (u, v) in data:
        degree[u] += 1
        degree[v] += 1
    for tup in data: # リストの各タプルに対して
        if model=="IC":
            edges_M[(tup[0], tup[1])] = 0.1# カスケードAのエッジ (u, v) の重みを入次数で割って求める
            edges_C[(tup[0], tup[1])] = 0.05 # カスケードBのエッジ (u, v) の重みを入次数の2倍で割って求める
            edges_M[(tup[1], tup[0])] = 0.1 # カスケードAのエッジ (v, u) の重みを入次数で割って求める
            edges_C[(tup[1], tup[0])] = 0.05 # カスケードBのエッジ (v, u) の重みを入次数の2倍で割って求める
        if model=="WC":
            edges_M[(tup[0], tup[1])] = 1 / degree[tup[1]] # カスケードAのエッジ (u, v) の重みを入次数で割って求める
            edges_M[(tup[1], tup[0])] = 1 / degree[tup[0]] # カスケードAのエッジ (v, u) の重みを入次数で割って求める
            edges_C[(tup[0], tup[1])] = 1 / (2 * degree[tup[1]]) # カスケードBのエッジ (u, v) の重みを入次数の2倍で割って求める
            edges_C[(tup[1], tup[0])] = 1 / (2 * degree[tup[0]]) # カスケードBのエッジ (v, u) の重みを入次数の2倍で割って求める
    return nodes, edges_M, edges_C,degree,n,data
