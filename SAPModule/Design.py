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
    