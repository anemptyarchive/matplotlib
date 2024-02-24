
# 2次元(2方向)ランダムウォークの作図

# %%

# 利用するライブラリ
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# %%

### 乱数の生成

# 試行回数を指定
max_iter = 600

# サンプルサイズを指定
sample_size = 5

# 乱数を生成
random_val_arr  = np.random.choice([-1, 1], size=(sample_size, max_iter), replace=True) # 移動量
random_axis_arr = np.random.choice(['x', 'y'], size=(sample_size, max_iter), replace=True) # 移動軸

# 試行ごとに集計
x_arr = np.cumsum(
    np.hstack([np.zeros((sample_size, 1)), np.int32(random_axis_arr=='x') * random_val_arr]), # 初期値を追加
    axis=1
)
y_arr = np.cumsum(
    np.hstack([np.zeros((sample_size, 1)), np.int32(random_axis_arr=='y') * random_val_arr]), # 初期値を追加
    axis=1
)

# %%

### グラフの作図：(座標軸のみ)

# グラフサイズを設定
margin_rate = 0.1
axis_size = np.max([np.abs(x_arr), np.abs(y_arr)])
axis_size = np.ceil(axis_size * (1+margin_rate)) # 余白を追加

# 2Dランダムウォークを作図
fig, ax = plt.subplots(figsize=(10, 10), facecolor='white')
ax.axhline(y=0, color='red', linestyle='dashed') # 初期値
ax.axvline(x=0, color='red', linestyle='dashed') # 初期値
ax.plot(x_arr.T, y_arr.T, alpha=0.4) # 軌跡
for s in range(sample_size):
    ax.scatter(x_arr[s, max_iter], y_arr[s, max_iter], s=100, zorder=10) # 最終地点
ax.set_xlim(xmin=-axis_size, xmax=axis_size)
ax.set_ylim(ymin=-axis_size, ymax=axis_size)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('iteration: '+str(max_iter), loc='left')
fig.suptitle('Random Walk', fontsize=20)
ax.grid()
ax.set_aspect('equal')

# グラフを書出
plt.savefig(fname='../figure/RandomWalk/2d_90_xy_n.png', dpi=250)

plt.show()

# %%

### アニメーションの作図：(座標軸のみ)

# グラフサイズを設定
margin_rate = 0.1
axis_size = np.ceil(np.max([np.abs(x_arr), np.abs(y_arr)]))
axis_size = np.ceil(axis_size * (1+margin_rate)) # 余白を追加

# グラフオブジェクトを初期化
fig, ax = plt.subplots(figsize=(10, 10), facecolor='white')
fig.suptitle('Random Walk', fontsize=20)

# 作図処理を定義
def update(i):
    
    # 前フレームのグラフを初期化
    plt.cla()
    
    # 2Dランダムウォークを作図
    ax.axhline(y=0, color='red', linestyle='dashed') # 初期値
    ax.axvline(x=0, color='red', linestyle='dashed') # 初期値
    ax.plot(x_arr.T[:i+1], y_arr.T[:i+1], alpha=0.4) # 軌跡
    for s in range(sample_size):
        ax.scatter(x_arr[s, i], y_arr[s, i], s=100, zorder=10) # 現在地点
    ax.set_xlim(xmin=-axis_size, xmax=axis_size)
    ax.set_ylim(ymin=-axis_size, ymax=axis_size)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('iteration: '+str(i), loc='left')
    ax.grid()
    ax.set_aspect('equal')

# 動画を作成
ani = FuncAnimation(fig=fig, func=update, frames=max_iter+1, interval=100)

# 動画を書出
ani.save(
    filename='../figure/RandomWalk/2d_90_xy_n.mp4', dpi=250, 
    progress_callback = lambda i, n: print(f'frame: {i} / {n}')
)

# %%

### グラフの作成：(サンプル軸あり)

# グラフサイズを設定
margin_rate = 0.1
axis_size  = np.max([np.abs(x_arr), np.abs(y_arr)])
axis_size  = np.ceil(axis_size * (1+margin_rate)) # 余白を追加
axis_s_min = -sample_size * margin_rate # 余白を追加

# 配色の共通化用のカラーマップを作成
cmap = plt.get_cmap("tab10")
color_num = 10 # カラーマップごとに固定

# 2Dランダムウォークを作図
fig, ax = plt.subplots(figsize=(12, 12), facecolor='white', 
                       subplot_kw={'projection': '3d'})
for s in range(sample_size):

    # 最終値を取得
    x = x_arr[s, max_iter]
    y = y_arr[s, max_iter]

    ax.plot(x_arr[s], y_arr[s], zs=axis_s_min, zdir='z', 
            color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # xy面の軌跡
    ax.plot(x_arr[s], np.repeat(s+1, repeats=max_iter+1), zs=axis_size, zdir='y', 
            color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # x面の軌跡
    ax.plot(y_arr[s], np.repeat(s+1, repeats=max_iter+1), zs=-axis_size, zdir='x', 
            color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # y面の軌跡
    ax.scatter([x, x, -axis_size], 
               [y, axis_size, y], 
               [axis_s_min, s+1, s+1], 
               s=100, fc='none', ec=cmap(s%color_num)) # 面ごとの最終地点
    ax.quiver(x, y, s+1, 
              [0, -axis_size-x, 0], [0, 0, axis_size-y], [axis_s_min-s-1, 0, 0], 
              arrow_length_ratio=0, color=cmap(s%color_num), linewidth=1, linestyle='dotted') # 点の目盛線
    ax.plot(x_arr[s], y_arr[s], s+1, color=cmap(s%color_num), alpha=0.4) # 軌跡
    ax.scatter(x, y, s+1, color=cmap(s%color_num), s=100) # 最終地点
ax.margins(x=0.0, y=0.0, z=0.0) # (機能しない?のでlimで謎小細工)
ax.set_xlim(xmin=-axis_size/1.05, xmax=axis_size/1.05)
ax.set_ylim(ymin=-axis_size/1.05, ymax=axis_size/1.05)
ax.set_zlim(zmin=axis_s_min, zmax=sample_size+1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('sample')
ax.set_title('iteration: '+str(max_iter), loc='left')
fig.suptitle('Random Walk', fontsize=20)
ax.set_box_aspect((1, 1, 0.5))
ax.view_init(elev=10, azim=300) # 表示アングル

# グラフを書出
plt.savefig(fname='../figure/RandomWalk/2d_90_xys_n.png', dpi=250)

plt.show()

# %%

### アニメーションの作成：(サンプル軸あり)

# グラフサイズを設定
margin_rate = 0.1
axis_size  = np.max([np.abs(x_arr), np.abs(y_arr)])
axis_size  = np.ceil(axis_size * (1+margin_rate)) # 余白を追加
axis_s_min = -sample_size * margin_rate # 余白を追加

# グラフオブジェクトを初期化
fig, ax = plt.subplots(figsize=(12, 12), facecolor='white', 
                       subplot_kw={'projection': '3d'})
fig.suptitle('Random Walk', fontsize=20)

# 配色の共通化用のカラーマップを作成
cmap = plt.get_cmap("tab10")
color_num = 10 # カラーマップごとに固定

# 作図処理を定義
def update(i):
    
    # 前フレームのグラフを初期化
    plt.cla()
    
    # 2Dランダムウォークを作図
    for s in range(sample_size):

        # 現在値を取得
        x = x_arr[s, i]
        y = y_arr[s, i]
        
        ax.plot(x_arr[s, :i+1], y_arr[s, :i+1], zs=axis_s_min, zdir='z', 
                color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # xy面の軌跡
        ax.plot(x_arr[s, :i+1], np.repeat(s+1, repeats=i+1), zs=axis_size, zdir='y', 
                color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # x面の軌跡
        ax.plot(y_arr[s, :i+1], np.repeat(s+1, repeats=i+1), zs=-axis_size, zdir='x', 
                color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # y面の軌跡
        ax.scatter([x, x, -axis_size], 
                   [y, axis_size, y], 
                   [axis_s_min, s+1, s+1], 
                   s=100, fc='none', ec=cmap(s%color_num)) # 面ごとの現在地点
        ax.quiver(x, y, s+1, 
                  [0, -axis_size-x, 0], [0, 0, axis_size-y], [axis_s_min-s-1, 0, 0], 
                  arrow_length_ratio=0, color=cmap(s%color_num), linewidth=1, linestyle='dotted') # 点の目盛線
        ax.plot(x_arr[s, :i+1], y_arr[s, :i+1], s+1, color=cmap(s%color_num), alpha=0.4) # 軌跡
        ax.scatter(x, y, s+1, color=cmap(s%color_num), s=100) # 現在地点
    ax.margins(x=0.0, y=0.0, z=0.0) # (機能しない?のでlimで謎小細工)
    ax.set_xlim(xmin=-axis_size/1.05, xmax=axis_size/1.05)
    ax.set_ylim(ymin=-axis_size/1.05, ymax=axis_size/1.05)
    ax.set_zlim(zmin=axis_s_min, zmax=sample_size+1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('sample')
    ax.set_title('iteration: '+str(i), loc='left')
    ax.set_box_aspect((1, 1, 0.5))
    ax.view_init(elev=30, azim=i) # 表示アングル

# 動画を作成
ani = FuncAnimation(fig=fig, func=update, frames=max_iter+1, interval=100)

# 動画を書出
ani.save(
    filename='../figure/RandomWalk/2d_90_xys_n.mp4', dpi=250, 
    progress_callback = lambda i, n: print(f'frame: {i} / {n}')
)

# %%

### グラフの作成：(時間軸あり)

# グラフサイズを設定
margin_rate = 0.1
axis_size  = np.max([np.abs(x_arr), np.abs(y_arr)])
axis_size  = np.ceil(axis_size * (1+margin_rate)) # 余白を追加
axis_i_min = -max_iter * margin_rate    # 余白を追加
axis_i_max = max_iter * (1+margin_rate) # 余白を追加

# 配色の共通化用のカラーマップを作成
cmap = plt.get_cmap("tab10")
color_num = 10 # カラーマップごとに固定

# 2Dランダムウォークを作図
fig, ax = plt.subplots(figsize=(15, 14), facecolor='white', 
                       subplot_kw={'projection': '3d'})
for s in range(sample_size):

    # 最終値を取得
    x = x_arr[s, max_iter]
    y = y_arr[s, max_iter]

    ax.plot(x_arr[s], y_arr[s], zs=axis_i_min, zdir='x', 
            color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # xy面の軌跡
    ax.plot(np.arange(max_iter+1), x_arr[s], zs=-axis_size, zdir='z', 
            color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # ix面の軌跡
    ax.plot(np.arange(max_iter+1), y_arr[s], zs=axis_size, zdir='y', 
            color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # iy面の軌跡
    ax.scatter([axis_i_min, max_iter, max_iter], 
               [x, x, axis_size], 
               [y, -axis_size, y], 
               s=100, fc='none', ec=cmap(s%color_num)) # 面ごとの最終地点
    ax.quiver(max_iter, x, y, 
              [axis_i_min-max_iter, 0, 0], [0, 0, axis_size-x], [0, -axis_size-y, 0], 
              arrow_length_ratio=0, color=cmap(s%color_num), linewidth=1, linestyle='dotted') # 点の目盛線
    ax.plot(np.arange(max_iter+1), x_arr[s], y_arr[s], color=cmap(s%color_num), alpha=0.4) # 軌跡
    ax.scatter(max_iter, x, y, color=cmap(s%color_num), s=100) # 最終地点
ax.margins(x=0.0, y=0.0, z=0.0) # (機能しない?のでlimで謎小細工)
ax.set_xlim(xmin=axis_i_min+axis_i_max*0.025, xmax=axis_i_max)
ax.set_ylim(ymin=-axis_size/1.05, ymax=axis_size/1.05)
ax.set_zlim(zmin=-axis_size/1.05, zmax=axis_size/1.05)
ax.set_xlabel('iteration')
ax.set_ylabel('x')
ax.set_zlabel('y')
ax.set_title('iteration: '+str(max_iter), loc='left')
fig.suptitle('Random Walk', fontsize=20)
ax.set_box_aspect((2, 1, 1))
#ax.view_init(elev=0, azim=0) # 表示アングル

# グラフを書出
plt.savefig(fname='../figure/RandomWalk/2d_90_ixy_n.png', dpi=250)

plt.show()

# %%

### アニメーションの作成：(時間軸あり)

# グラフサイズを設定
margin_rate = 0.1
axis_size  = np.max([np.abs(x_arr), np.abs(y_arr)])
axis_size  = np.ceil(axis_size * (1+margin_rate)) # 余白を追加
axis_i_min = -max_iter * margin_rate    # 余白を追加
axis_i_max = max_iter * (1+margin_rate) # 余白を追加

# グラフオブジェクトを初期化
fig, ax = plt.subplots(figsize=(15, 14), facecolor='white', 
                       subplot_kw={'projection': '3d'})
fig.suptitle('Random Walk', fontsize=20)

# 配色の共通化用のカラーマップを作成
cmap = plt.get_cmap("tab10")
color_num = 10 # カラーマップごとに固定

# 作図処理を定義
def update(i):
    
    # 前フレームのグラフを初期化
    plt.cla()
    
    # 2Dランダムウォークを作図
    for s in range(sample_size):

        # 現在値を取得
        x = x_arr[s, i]
        y = y_arr[s, i]
        
        ax.plot(x_arr[s, :i+1], y_arr[s, :i+1], zs=axis_i_min, zdir='x', 
                color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # xy面の軌跡
        ax.plot(np.arange(i+1), x_arr[s, :i+1], zs=-axis_size, zdir='z', 
                color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # ix面の軌跡
        ax.plot(np.arange(i+1), y_arr[s, :i+1], zs=axis_size, zdir='y', 
                color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # iy面の軌跡
        ax.scatter([axis_i_min, i, i], 
                   [x, x, axis_size], 
                   [y, -axis_size, y], 
                   s=100, fc='none', ec=cmap(s%color_num)) # 面ごとの現在地点
        ax.quiver(i, x, y, 
                  [axis_i_min-i, 0, 0], [0, 0, axis_size-x], [0, -axis_size-y, 0], 
                  arrow_length_ratio=0, color=cmap(s%color_num), linewidth=1, linestyle='dotted') # 点の目盛線
        ax.plot(np.arange(i+1), x_arr[s, :i+1], y_arr[s, :i+1], color=cmap(s%color_num), alpha=0.4) # 軌跡
        ax.scatter(i, x, y, color=cmap(s%color_num), s=100) # 現在地点
    ax.margins(x=0.0, y=0.0, z=0.0) # (機能しない?のでlimで謎小細工)
    ax.set_xlim(xmin=axis_i_min+axis_i_max*0.025, xmax=axis_i_max)
    ax.set_ylim(ymin=-axis_size/1.05, ymax=axis_size/1.05)
    ax.set_zlim(zmin=-axis_size/1.05, zmax=axis_size/1.05)
    ax.set_xlabel('iteration')
    ax.set_ylabel('x')
    ax.set_zlabel('y')
    ax.set_title('iteration: '+str(i), loc='left')
    ax.set_box_aspect((2, 1, 1))
    #ax.view_init(elev=30, azim=180+i) # 表示アングル

# 動画を作成
ani = FuncAnimation(fig=fig, func=update, frames=max_iter+1, interval=100)

# 動画を書出
ani.save(
    filename='../figure/RandomWalk/2d_90_ixy_n.mp4', dpi=250, 
    progress_callback = lambda i, n: print(f'frame: {i} / {n}')
)

# %%


