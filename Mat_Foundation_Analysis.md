
# Mat Foundation Analysis and Design using SAP2000

__Gitamondoc Gopaoco Structural Engineering__

__Engr. Michael James C. Quidilla, CE__

_Updated: November 09, 2017_

## Assumptions for the Model

### Model definition

- Allowable Bearing Capaicty = $ 200 kPa $

- Allowable deflection of soil = $ 10mm $

- Spring stiffness coefficient = $ 200kPa $ / $ 10mm $ = $ 200000kN/m^3 $

- Thickness of foundation = $ 1.50m $

- Keep in mind that the results of SAP2000 from the table if extracted via Resultant forces are in kN/m or kN*m/m. SAP2000 divided by a __tributary width of 1m__. The result must then be multiplied by the __tributary area__ of the resultant force or moment.

- The Earthquake was neglected on the analysis due the fact that column load combination are governed by Dead plus Live. The governing shearwall combination includes EQX and EQY. But the analysis is focused on the positive and negative steel reinforcements per column on top of the mat.

- The stresses were extracted from SAP2000 via tables and plotted here for better visualization.


The verification of modeling of the mat foundation was modeled initially with a isolated footing and compared it with its RCD counter part. The results summary are as follows:

- the Ultimate bearing capacity $(Pu/Ag)$ distributed along the isolated footing of the SAP2000 model were exactly the same as the RCD's Ultimate bearing capacity. The difference in the bearing capacity is that the SAP2000 model's spring reaction (idealized from the soil pressure reaction) are more distributed in a circular manner than the RCD's approach which is distributed evenly. 

- The Moment and punching shear of the SAP2000 model are nearly identical compared to the RCD's approach. The computation of the moment is at the critical section (at the face of the column for moment and column dimension C + d (depth of footing) distance from the center of the column for critical punching area for shear)

# Exploration of the Data

## Summary Statistics of the Mat Foundation Ultimate Bearing Capacity


```python
import pandas as pd
```


```python
reactions = pd.read_excel('MatFoundationReactions-1500mm.xlsx')
```


```python
reactions.describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Joint</th>
      <th>GlobalX (mm)</th>
      <th>GlobalY (mm)</th>
      <th>Dead (kN)</th>
      <th>EQX (kN)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>463.959459</td>
      <td>9551.041667</td>
      <td>15132.162162</td>
      <td>144.930963</td>
      <td>35.655324</td>
    </tr>
    <tr>
      <th>std</th>
      <td>257.418111</td>
      <td>5909.219702</td>
      <td>8938.546894</td>
      <td>46.321112</td>
      <td>35.734753</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>8.828000</td>
      <td>-29.239000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>242.750000</td>
      <td>4475.000000</td>
      <td>7843.330000</td>
      <td>121.683000</td>
      <td>6.940750</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>464.500000</td>
      <td>9425.000000</td>
      <td>14773.330000</td>
      <td>155.777500</td>
      <td>31.280000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>686.250000</td>
      <td>14490.625000</td>
      <td>22750.000000</td>
      <td>177.992750</td>
      <td>61.144000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>908.000000</td>
      <td>19500.000000</td>
      <td>30700.000000</td>
      <td>216.582000</td>
      <td>135.156000</td>
    </tr>
  </tbody>
</table>
</div>



## Plotting the Heat map of the Ultimate Beariing Capacity of Mat Foundation Based of Dead + Live


```python
plot_contour_map(file_name='MatFoundationReactions-1500mm.xlsx',
                stress_name = 'Dead (kN)',
                level = [0, 220, 30],
                color = 'nipy_spectral',
                title = 'Oakrdige Building 2: Ultimate Bearing Capacity of Mat Foundation Heat Map',
                fsize = [15,15])
```


![png](Mat_Foundation_Analysis_files/Mat_Foundation_Analysis_10_0.png)


## Summary Statistics of the Mat Foundation Shell Forces


```python
shell_forces = pd.read_excel('ShellForcesCLEAN-1500mm.xlsx')
```


```python
shell_forces.describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Joint</th>
      <th>GlobalX (mm)</th>
      <th>GlobalY (mm)</th>
      <th>F11</th>
      <th>F22</th>
      <th>F12</th>
      <th>FMax</th>
      <th>FMin</th>
      <th>FAngle</th>
      <th>FVM</th>
      <th>M11</th>
      <th>M22</th>
      <th>M12</th>
      <th>MMax</th>
      <th>MMin</th>
      <th>MAngle</th>
      <th>V13</th>
      <th>V23</th>
      <th>VMax</th>
      <th>VAngle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
      <td>888.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>463.959459</td>
      <td>9551.041667</td>
      <td>15132.162162</td>
      <td>23.028826</td>
      <td>-9.630043</td>
      <td>0.846994</td>
      <td>43.554174</td>
      <td>-30.155535</td>
      <td>0.323122</td>
      <td>72.071122</td>
      <td>628.123909</td>
      <td>252.299246</td>
      <td>2.110660</td>
      <td>739.293697</td>
      <td>141.129456</td>
      <td>-3.471924</td>
      <td>-8.397617</td>
      <td>-6.917992</td>
      <td>422.129671</td>
      <td>-1.421440</td>
    </tr>
    <tr>
      <th>std</th>
      <td>257.418111</td>
      <td>5909.219702</td>
      <td>8938.546894</td>
      <td>59.642665</td>
      <td>71.201937</td>
      <td>31.384247</td>
      <td>55.449521</td>
      <td>88.068414</td>
      <td>42.668738</td>
      <td>113.279964</td>
      <td>538.808755</td>
      <td>502.471305</td>
      <td>158.074327</td>
      <td>539.163111</td>
      <td>442.631580</td>
      <td>37.261246</td>
      <td>363.124529</td>
      <td>357.849489</td>
      <td>481.578875</td>
      <td>95.332948</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-331.550000</td>
      <td>-610.381667</td>
      <td>-157.791667</td>
      <td>-33.100000</td>
      <td>-839.435000</td>
      <td>-89.402000</td>
      <td>0.010560</td>
      <td>-81.734350</td>
      <td>-628.994300</td>
      <td>-591.538675</td>
      <td>-28.802850</td>
      <td>-629.168975</td>
      <td>-89.499000</td>
      <td>-2327.440000</td>
      <td>-2369.987500</td>
      <td>5.740000</td>
      <td>-175.304500</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>242.750000</td>
      <td>4475.000000</td>
      <td>7843.330000</td>
      <td>-1.010000</td>
      <td>-4.736875</td>
      <td>-5.561250</td>
      <td>7.500625</td>
      <td>-21.881875</td>
      <td>-27.880562</td>
      <td>11.867500</td>
      <td>226.233469</td>
      <td>-52.960000</td>
      <td>-78.107894</td>
      <td>389.348038</td>
      <td>-101.041681</td>
      <td>-21.153500</td>
      <td>-155.916250</td>
      <td>-145.062500</td>
      <td>170.406875</td>
      <td>-85.078500</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>464.500000</td>
      <td>9425.000000</td>
      <td>14773.330000</td>
      <td>5.628750</td>
      <td>0.581250</td>
      <td>0.210000</td>
      <td>24.952500</td>
      <td>-6.831250</td>
      <td>0.536850</td>
      <td>32.021250</td>
      <td>565.267787</td>
      <td>188.591850</td>
      <td>-7.379187</td>
      <td>648.303488</td>
      <td>65.744512</td>
      <td>-1.442375</td>
      <td>-26.580000</td>
      <td>0.235000</td>
      <td>286.978750</td>
      <td>-0.512125</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>686.250000</td>
      <td>14490.625000</td>
      <td>22750.000000</td>
      <td>37.054375</td>
      <td>12.420000</td>
      <td>6.774375</td>
      <td>56.845625</td>
      <td>-1.806875</td>
      <td>28.881375</td>
      <td>75.271875</td>
      <td>873.664975</td>
      <td>464.040735</td>
      <td>88.606700</td>
      <td>970.014762</td>
      <td>318.922388</td>
      <td>14.985750</td>
      <td>155.240625</td>
      <td>139.566250</td>
      <td>473.906250</td>
      <td>73.495437</td>
    </tr>
    <tr>
      <th>max</th>
      <td>908.000000</td>
      <td>19500.000000</td>
      <td>30700.000000</td>
      <td>305.281667</td>
      <td>84.335000</td>
      <td>158.472500</td>
      <td>310.683333</td>
      <td>45.007500</td>
      <td>88.856250</td>
      <td>889.335000</td>
      <td>4982.597425</td>
      <td>4151.461700</td>
      <td>541.670875</td>
      <td>5015.867975</td>
      <td>4118.191100</td>
      <td>89.356000</td>
      <td>2189.277500</td>
      <td>2075.260000</td>
      <td>4393.025000</td>
      <td>178.232000</td>
    </tr>
  </tbody>
</table>
</div>



## Plotting the Contour Map of  Axial Factored Dead + Live load of Mat Foundation

## Design of Steel along X-Direction


```python
plot_contour_map(file_name='ShellForcesCLEAN-1500mm.xlsx',
                stress_name = 'M11',
                level = [-100, 5000, 30],
                color = 'nipy_spectral',
                title = 'Oakrdige Building 2: Factored Moment (kN.m / m) Along X-axis Factored Dead + Live Stresses on Mat Foundation Heat Map',
                fsize = [15,15])
```


![png](Mat_Foundation_Analysis_files/Mat_Foundation_Analysis_16_0.png)


__Maximum Bottom bar reinforcement for C6 and C14:__


```python
Moment = 1.62*1.39*5000
design_steel_rein(Mu = Moment, b = 3*1620, d = 1500, db = 28, layers = 1, cover = 75)
```

    p: 0.003130069464583729
    pmin:  0.0034
    4/3*p:  0.0042
    usep:  0.0034
    Moment:  11259.00, no of bars: 38 using  28 mm rebar 1 layers
    spacing:  135 mm
    

__Maximum Bottom bar reinforcement for C24, C25, C19, C15 and C7:__


```python
Moment = 1.62*1.39*3000
design_steel_rein(Mu = Moment, b = 5200, d = 1500, db = 28, layers = 1, cover = 75)
```

    p: 0.0017380376821601482
    pmin:  0.0034
    4/3*p:  0.0023
    usep:  0.0023
    Moment:  6755.40, no of bars: 28 using  28 mm rebar 1 layers
    spacing:  158 mm
    

__Maximum Bottom bar reinforcement for C11 and C13:__


```python
Moment = 1.62*1.39*800
design_steel_rein(Mu = Moment, b = 2*1620, d = 1500, db = 28, layers = 1, cover = 75)
```

    p: 0.0007386522711734751
    pmin:  0.0034
    4/3*p:  0.0010
    usep:  0.0020
    Moment:  1801.44, no of bars: 15 using  28 mm rebar 1 layers
    spacing:  99 mm
    

## Design of Steel along Y-Direction


```python
plot_contour_map(file_name='ShellForcesCLEAN-1500mm.xlsx',
                stress_name = 'M22',
                level = [-650, 4200, 50],
                color = 'nipy_spectral',
                title = 'Oakrdige Building 2: Factored Moment (kN.m / m) Along Y-axis Factored Dead + Live Stresses on Mat Foundation Heat Map',
                fsize = [15,15])
```


![png](Mat_Foundation_Analysis_files/Mat_Foundation_Analysis_24_0.png)


__Maximum Bottom bar reinforcement for C6 and C14__


```python
Moment = 1.32*1.62*3500
design_steel_rein(Mu = Moment, b = 4*1390, d = 1500, db = 28, layers = 1, cover = 75)
```

    p: 0.0018017250286220137
    pmin:  0.0034
    4/3*p:  0.0024
    usep:  0.0024
    Moment:  7484.40, no of bars: 31 using  28 mm rebar 1 layers
    spacing:  168 mm
    

__Maximum Bottom bar reinforcement for C19, C24, and C25__


```python
Moment = 3*1.32*1.62*2500
design_steel_rein(Mu = Moment, b = 4*1390, d = 1500, db = 28, layers = 1, cover = 75)
```

    p: 0.003919320516904343
    pmin:  0.0034
    4/3*p:  0.0052
    usep:  0.0039
    Moment:  16038.00, no of bars: 50 using  28 mm rebar 1 layers
    spacing:  148 mm
    

__Maximum Bottom bar reinforcement for C7 and C15__


```python
Moment = 1.32*3*1.62*3000
design_steel_rein(Mu = Moment, b = 4*1390, d = 1500, db = 28, layers = 1, cover = 75)
```

    p: 0.004730638398353554
    pmin:  0.0034
    4/3*p:  0.0063
    usep:  0.0047
    Moment:  19245.60, no of bars: 61 using  28 mm rebar 1 layers
    spacing:  137 mm
    

__Maximum Top bar reinforcement for Mat Foundation both ways__


```python
Moment = 1.32*3*600*1.62
design_steel_rein(Mu = Moment, b = 4*1390, d = 1500, db = 28, layers = 1, cover = 75)
```

    p: 0.000920885805596799
    pmin:  0.0034
    4/3*p:  0.0012
    usep:  0.0020
    Moment:  3849.12, no of bars: 26 using  28 mm rebar 1 layers
    spacing:  174 mm
    


```python
plot_contour_map(file_name='ShellForcesCLEAN-1500mm.xlsx',
                stress_name = 'VMax',
                level = [5, 4400, 30],
                color = 'nipy_spectral',
                title = 'Oakrdige Building 2: Maximum Punching Shear Force (kN / m) on Mat Foundation Heat Map',
                fsize = [15,15])
```


![png](Mat_Foundation_Analysis_files/Mat_Foundation_Analysis_33_0.png)



```python
def plot_contour_map(file_name, stress_name, level, color, title, fsize): 
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
    %matplotlib inline
    
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
        ax.annotate(txt, (a[i]+0.2, b[i]+0.2))
        
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
    ax.annotate('SW-1', (6.5,14.54))
    
    # plotting Shearwall SW-2 as lines
    line6 = lines.Line2D([4.552,4.552],[6.11,9.06], linewidth=7, color='white', alpha = 0.5)
    line7 = lines.Line2D([12.502,12.502],[6.11,9.06], linewidth=7, color='white', alpha = 0.5)
    line8 = lines.Line2D([4.552,12.502],[6.11,6.11], linewidth=7, color='white', alpha = 0.5)
    ax.add_line(line6)
    ax.add_line(line7)
    ax.add_line(line8)
    ax.annotate('SW-2', (7.8,7.5))

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
                 shrink=0.50)

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
```


```python
def design_steel_rein(Mu, b, d, db, layers, cover):
    '''
    Design the steel reinforment based on Moment
    Mu = Factored moment (kN*m)
    b = base (mm)
    d = depth (mm)
    db = bar diameter (mm)
    cover = concrete cover (mm)
    '''
    d = d - cover
    fy = 414
    fc = 35
    m = fy / 0.85 / fc
    Ru = Mu * 10**6 / 0.9 / b / d**2
    p = 1/m * (1-(1-2*Ru*m/fy)**0.5)
    pmin = min((0.25 * (fc)**0.5 / fy),(1.4/fy))
    
    if p > pmin:
        usep = p
    elif p < pmin:
        usep = min(4/3*p, pmin)
        usep = max(usep, 0.002)
    else:
        usep = pmin
        
    As = usep * b * d
    Ab = 3.14159*db**2/4 * layers
    spacing = (b - 2*cover-(As/Ab)*db)/(db-1)
    
    print('p: {0}'.format(p))
    print('pmin: {0: 0.4f}'.format(pmin))
    print('4/3*p: {0: 0.4f}'.format(4/3*p))
    print('usep: {0: 0.4f}'.format(usep))
    print('Moment: {0: 0.2f}, no of bars:{1: 0.0f} using {2: 0.0f} mm rebar {3} layers'.format(Mu, As/Ab, db, layers))
    print('spacing: {0: 0.0f} mm'.format(spacing))
    
    return 
    
```
