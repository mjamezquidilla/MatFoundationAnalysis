def plot_contour_map(file_name, stress_name, level, color, title, fsize, contour_level=10): 
    '''
    file_name: name of dataframe to use
    stress_name: name of stresses or forces to by analyzed
    level = level or range of stresses and its interval. List.
    color = color or contour map for cmap. e.g. plt.cm.Spectral.
    title = title of chart. String.
    fzise = figure size. List
    '''
    # import statements
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import matplotlib.tri as tri
    import pandas as pd
    import matplotlib.lines as lines
    
    # reading data from excel and converting it to pandas dataframe
    df = pd.read_excel(file_name, index_col='Joint')

    sns.set(style="white")

    # mesh values
    x = df['GlobalX (mm)']/1000
    y = df['GlobalY (mm)']/1000
    z = df[stress_name]

    # making figure to plot on
    fig = plt.figure(figsize=fsize)
    ax = fig.add_subplot(111)

    # plotting columns
    plt.plot(8, 26.9, marker='o', markersize=10, color="white", zorder = 15, label ='C6', alpha = 0.5)
    plt.plot(16, 26.9, marker='o', markersize=10, color="white", zorder = 15, label ='C7', alpha = 0.5)
    plt.plot(4.1, 22.75, marker='o', markersize=10, color="white", zorder = 15, label ='C11', alpha = 0.5)
    plt.plot(4.1, 18.9, marker='o', markersize=10, color="white", zorder = 15, label ='C13', alpha = 0.5)
    plt.plot(8, 18.9, marker='o', markersize=10, color="white", zorder = 15, label ='C14', alpha = 0.5)
    plt.plot(16, 18.9, marker='o', markersize=10, color="white", zorder = 15, label ='C15', alpha = 0.5)
    plt.plot(16, 10.9, marker='o', markersize=10, color="white", zorder = 15, label ='C19', alpha = 0.5)
    plt.plot(8, 2.9, marker='o', markersize=10, color="white", zorder = 15, label ='C24', alpha = 0.5)
    plt.plot(16, 2.9, marker='o', markersize=10, color="white", zorder = 15, label ='C25', alpha = 0.5)

    # annotating columns
    n = ['C6','C7', 'C11', 'C13', 'C14', 'C15', 'C19', 'C24', 'C25']
    a = [8,16,4.1,4.1,8,16,16,8,16]
    b = [26.9,26.9,22.75,18.9,18.9,18.9,10.9,2.9,2.9]
    for i, txt in enumerate(n):
        ax.annotate(txt, (a[i]+0.2, b[i]+0.2), color = 'white')
        
    # plotting Shearwall SW-1 as lines
    line1 = lines.Line2D([4.552,4.552],[13.24,16.19], linewidth=7, color='white', alpha = 0.5)
    line2 = lines.Line2D([4.552,9.852],[16.19,16.19], linewidth=7, color='white', alpha = 0.5)
    line3 = lines.Line2D([9.852,9.852],[13.24,16.90], linewidth=7, color='white', alpha = 0.5)
    line4 = lines.Line2D([12.502,12.502],[13.24,16.90], linewidth=7, color='white', alpha = 0.5)
    line5 = lines.Line2D([9.852,12.502],[16.90,16.90], linewidth=7, color='white', alpha = 0.5)
    ax.add_line(line1)
    ax.add_line(line2)
    ax.add_line(line3)
    ax.add_line(line4)
    ax.add_line(line5)
    ax.annotate('SW-1', (6.5,14.54), color = 'white')
    
    # plotting Shearwall SW-2 as lines
    line6 = lines.Line2D([4.552,4.552],[6.11,9.06], linewidth=7, color='white', alpha = 0.5)
    line7 = lines.Line2D([12.502,12.502],[6.11,9.06], linewidth=7, color='white', alpha = 0.5)
    line8 = lines.Line2D([4.552,12.502],[6.11,6.11], linewidth=7, color='white', alpha = 0.5)
    ax.add_line(line6)
    ax.add_line(line7)
    ax.add_line(line8)
    ax.annotate('SW-2', (7.8,7.5), color = 'white')

    # making plot mesh and interpolation of x,y and z values for contour map
    nptsx, nptsy = len(x), len(y)
    xg, yg = np.meshgrid(np.linspace(x.min(), x.max(), nptsx),
                         np.linspace(y.min(), y.max(), nptsy))

    triangles = tri.Triangulation(x, y)
    tri_interp = tri.CubicTriInterpolator(triangles, z)
    zg = tri_interp(xg, yg)

    # change levels here according to your data
    levels = np.linspace(level[0], level[1], level[2])
    colormap = ax.contourf(xg, yg, zg, levels,
                           cmap=color,
                           norm=plt.Normalize(vmax=z.max(), vmin=z.min()),
                           zorder = 0)

    # add a colorbar
    fig.colorbar(colormap,
                 orientation='vertical',  # horizontal colour bar
                 shrink=1.0,
                 ticks=np.linspace(level[0], level[1], level[2]))
    
    # adding contour lines
    contours = plt.contour(xg, yg, zg, contour_level, colors='black')
    plt.clabel(contours, inline = True, fontsize = 10, fmt='%1.0f')


    # making gridlines
    plt.xticks(np.linspace(x.min(),x.max(),15))
    plt.yticks(np.linspace(y.min(),y.max(),20))
    ax.xaxis.grid(True, zorder=10, linestyle = '--', color = 'white', alpha = 0.2)
    ax.yaxis.grid(True, zorder=10, linestyle = '--', color = 'white', alpha = 0.2)
    ax.set_aspect("equal", "box")
    
    # plot title and label
    plt.title(title)
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')

    # show plot
    plt.show()