import numpy as np
import pandas as pd
import xarray as xr


def lat_time_data_sample():
    t = pd.DatetimeIndex(data=["2000-12-29", "2001-01-02", "2001-02-28", "2001-03-01"])
    y = [7.688, 9.562]
    x = [37.69, 39.56]
    # this is rr_mrg.sel(T=["2000-12-29", "2001-01-02", "2001-02-28", "2001-03-01"]).isel(X=[125, 175]).isel(Y=[125, 175]).precip
    # fmt: off
    values = [[[0.       ,  0.        ],
               [0.       ,  0.        ]],

              [[0.       ,  0.        ],
               [0.       ,  0.        ]],

              [[0.       ,  0.48477125],
               [0.99824536, 0.        ]],

              [[0.       ,  0.        ],
               [0.       ,  0.        ]]]
    # fmt: on
    precip = xr.DataArray(
        values, dims=["T", "Y", "X"], coords={"T": t, "Y": y, "X": x}
    ).rename("precip")
    precip["Y"].attrs = dict(units="degree_north")
    return precip


def multi_year_data_sample():
    t = pd.date_range(start="2000-01-01", end="2005-02-28", freq="1D")
    # this is rr_mrg.sel(T=slice("2000", "2005-02-28")).isel(X=150, Y=150).precip
    # fmt: off
    values = [
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.17853253,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.07629707,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.6139945 ,
        4.1458416 ,  1.8374273 ,  0.16281372,  0.02067695,  0.        ,
        1.7656178 ,  0.04611297,  0.        ,  0.        ,  0.        ,
        0.07533137,  0.        ,  0.00139176,  0.3145782 ,  0.        ,
        2.2567294 ,  9.710979  ,  2.2992668 ,  1.3868458 ,  0.67191434,
        0.5503186 ,  0.23389657,  6.0492983 ,  0.5441174 ,  0.23824258,
        0.        ,  0.0579729 ,  1.5021361 ,  0.9146768 ,  9.971033  ,
       12.578513  ,  4.084161  ,  8.318914  ,  9.434103  ,  6.5582333 ,
        4.1506906 ,  9.797739  ,  1.8234533 ,  1.5593919 ,  1.5255536 ,
        0.0332747 ,  0.00579074,  0.05337464,  0.03770629,  0.00037632,
        0.        ,  0.04690378,  0.01485118,  0.        ,  0.        ,
        0.        ,  0.        ,  0.01374616,  0.        ,  0.10477111,
        0.5504236 ,  0.48644277,  0.20262288,  0.15565012,  0.08816212,
        0.59143394,  0.48407283,  0.07558422,  0.        ,  1.550283  ,
        0.8879929 ,  2.1726742 ,  1.5877367 ,  3.4797363 ,  3.2136288 ,
        2.1750548 ,  0.7455304 ,  6.379514  ,  0.6569776 ,  0.15941368,
        6.430022  ,  0.43909433,  0.7460108 ,  0.28014034,  0.3459915 ,
        0.06514885,  8.082086  ,  0.14874002,  1.5860666 ,  1.009312  ,
        9.255059  ,  8.280125  ,  2.2002966 ,  5.011527  ,  3.0625327 ,
        6.342909  ,  3.067153  ,  9.136004  ,  4.827989  ,  6.755694  ,
        7.5010805 , 15.779922  , 17.708204  ,  2.3659167 ,  5.463901  ,
       12.58227   ,  0.69350517,  1.125054  ,  7.332282  ,  6.0628223 ,
        5.3329234 ,  6.4680347 ,  3.209999  ,  4.309499  ,  5.474716  ,
        9.741375  ,  9.016099  ,  3.9639661 ,  6.8523717 ,  3.4677095 ,
       11.144149  ,  3.083095  ,  7.2838783 ,  1.8788836 ,  9.365307  ,
        3.5578232 ,  6.0138106 ,  0.9172401 ,  4.1926255 ,  2.328648  ,
        2.3299572 ,  4.1698604 ,  3.988161  ,  5.2780204 ,  6.6621623 ,
        3.6110291 ,  3.0986016 ,  5.336749  ,  9.195411  ,  4.2239347 ,
        9.396879  ,  3.9909334 ,  1.4020501 ,  5.196463  ,  2.7474823 ,
        5.7457705 , 11.542407  ,  6.1288333 ,  8.348987  , 10.49291   ,
        1.4245225 ,  7.91107   ,  4.2546043 ,  3.1539578 ,  1.6214153 ,
        0.5971536 ,  0.84424335,  2.5041418 ,  1.2161577 ,  7.9344454 ,
        3.8384154 ,  0.8191301 ,  5.6934586 ,  8.180226  ,  4.933387  ,
        1.7886281 ,  1.9397591 ,  1.343717  ,  3.0967288 ,  4.014324  ,
        3.5429459 ,  3.2790685 ,  7.1374273 ,  0.3960947 ,  4.35338   ,
        2.4838953 ,  2.7103417 ,  5.4160175 ,  0.5115333 ,  0.42861763,
        3.202748  ,  0.25662202,  0.59925985,  0.991496  ,  5.7455387 ,
        1.7477425 ,  2.8542285 ,  4.077405  , 10.269378  ,  0.65223545,
        0.28262872,  2.408561  ,  2.2021687 ,  0.09267433,  0.01244594,
        0.04991561,  0.8169463 ,  0.2931116 ,  3.1355212 ,  0.07417266,
        0.00765838,  0.00111501,  0.01021147,  0.80279976,  0.1383777 ,
        0.        ,  0.3256596 ,  0.0344423 ,  0.21494202,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.09782565,  1.0059469 ,  0.301894  ,  0.        ,  0.18684903,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.17235592, 10.754777  ,  2.5819113 ,  0.13192528,
        1.5970107 ,  0.1977583 ,  0.        ,  0.        ,  0.        ,
        0.01773367,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.0597435 ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  1.4717993 ,  0.6891396 ,
        0.6538784 ,  1.3036579 ,  0.33328646,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.9108428 ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.07265995,  0.1426662 ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  1.2311451 ,  0.        ,  0.0721871 ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.15610833,  3.8392613 ,
        3.4286911 ,  0.941473  ,  0.01407858,  0.        ,  0.03028897,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.03001503,  0.7154983 ,  0.2877465 ,
        1.6761744 ,  0.7310815 ,  3.5253325 , 14.654359  , 13.009281  ,
        3.9350424 ,  5.8293214 ,  1.8313595 ,  0.13932733,  1.1262962 ,
        1.1623199 ,  0.91126394, 16.782093  ,  3.9347448 ,  0.02217657,
        0.        ,  0.0419644 ,  9.890126  ,  0.        ,  3.811365  ,
        0.5072849 ,  3.258365  ,  4.307502  ,  5.9564095 , 16.817566  ,
        3.2142677 ,  1.077374  ,  0.56219697,  0.        ,  0.00133954,
        0.02025914,  0.0159874 ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.00095772,  0.01702276,  0.04740249,
        0.40566674,  0.24028078,  0.        ,  0.        ,  0.        ,
        1.0683297 ,  3.446288  ,  0.08215389,  2.520098  ,  0.32259834,
        0.5440756 ,  0.        ,  0.3442291 ,  0.39248005,  1.3921894 ,
        0.6304584 ,  4.8525043 ,  1.5342025 ,  0.74660593,  0.        ,
       17.42565   ,  2.8061512 ,  0.00331392,  0.58463216,  6.5113077 ,
        7.5317173 ,  5.1354327 ,  2.4701855 ,  4.198995  ,  3.978146  ,
        6.0089397 ,  0.05982948,  0.00476582,  0.        ,  0.        ,
        0.        ,  0.        ,  0.21762428,  0.0207456 ,  0.06535809,
        0.        ,  3.8308804 ,  0.97331744,  5.4254165 ,  5.561438  ,
        0.        ,  0.47090462,  2.60351   ,  0.        ,  0.        ,
        0.17580006,  1.8115765 ,  3.5929682 , 11.917809  ,  3.8145216 ,
        3.1440992 ,  1.682752  ,  4.0080705 ,  4.26886   ,  0.93312544,
        2.2128162 ,  3.1299486 ,  3.843049  , 16.19793   ,  6.8482833 ,
        8.7324095 ,  4.580019  ,  2.5073404 ,  3.1874325 ,  3.464069  ,
        4.395224  ,  6.9638257 ,  7.0919046 ,  4.6538067 ,  0.36881235,
        3.5182903 ,  1.8570142 , 14.10599   ,  1.6169312 ,  2.5327997 ,
       14.228808  ,  9.237814  ,  0.3619393 ,  0.888819  ,  6.040326  ,
        7.7219863 ,  8.015229  ,  7.3416147 ,  2.2966132 , 11.926289  ,
       11.183476  ,  3.055649  ,  2.7075398 , 10.4243355 , 15.8988    ,
        8.938977  , 10.6758175 ,  0.02527452,  1.6654114 ,  7.2053475 ,
        9.195422  ,  7.8495374 , 10.389763  , 12.834826  ,  9.078284  ,
        4.9507823 ,  5.9971557 , 11.911917  , 11.1499195 ,  4.190289  ,
        2.2181165 ,  2.855249  ,  1.9984334 ,  1.3940252 ,  2.4264007 ,
        3.3736632 ,  5.0711446 ,  1.3100845 ,  0.9853619 ,  0.36709318,
        6.332088  ,  3.0051045 ,  1.2683933 ,  0.32189128,  3.7798853 ,
        6.025437  ,  1.5979156 ,  5.8544703 ,  4.2101426 ,  2.261607  ,
        4.939619  ,  0.03920667,  9.586336  ,  0.64533114,  1.5175112 ,
        1.0998025 ,  6.2961426 ,  4.6170278 ,  9.605053  ,  5.9746323 ,
        3.4905193 ,  0.02557231,  2.3422887 ,  1.2644733 ,  0.396759  ,
        0.5069229 ,  0.        ,  1.1464314 ,  0.69142586,  0.43347612,
        0.56379277,  2.1634603 ,  3.9481585 ,  3.8220766 ,  2.5631318 ,
        0.2569422 ,  0.        ,  0.11700156,  0.        ,  0.36121124,
        0.00028092,  0.4384375 ,  0.9238836 ,  0.        ,  0.        ,
        0.        ,  1.37263   ,  1.2380866 ,  0.53096336,  1.8594118 ,
        0.36269176,  0.        ,  0.        ,  0.00781125,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.02992022,  0.75541407,  0.        ,
        0.00732516,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.53944534,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.35578105,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.35735175,  0.        ,  0.        ,  0.08145782,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.26717094,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.00987519,  0.        ,  0.        ,  0.        ,  0.        ,
        1.7661523 ,  3.232971  , 24.468853  ,  4.874351  ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.1084196 ,  0.        ,
        0.        ,  9.835848  ,  4.7524056 ,  1.3340371 ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.70740426,
        0.06461952,  0.        ,  2.864181  ,  5.1746974 ,  3.1551697 ,
        0.0896953 ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.14720364,  4.835972  ,  4.71407   , 21.24237   ,  0.51080436,
        0.        ,  0.        ,  6.640717  ,  0.        ,  0.40124694,
        1.7016039 ,  0.        ,  0.        ,  0.        ,  5.261262  ,
        0.87570643,  1.4254671 ,  0.        ,  0.        ,  0.5449092 ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.40166956,  0.62819874,  0.41675147,  0.        ,  0.        ,
        0.85112685,  0.        ,  0.        ,  0.0561653 , 16.81271   ,
        0.2713415 ,  0.        ,  0.        ,  0.        ,  2.9465778 ,
        0.17977078,  0.04525282,  0.        ,  2.59189   ,  1.2182312 ,
        0.        ,  0.        ,  0.56799   ,  1.5948983 ,  2.8383482 ,
        0.25348482,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.04611551,  0.03531151,  1.6140708 ,  3.9210222 ,
        2.6270318 ,  1.0885324 ,  0.        ,  0.        ,  0.        ,
        0.22495624,  0.55089045,  0.        ,  0.        ,  0.        ,
        0.06853624,  0.90111023,  0.27357453,  0.15892597,  2.607463  ,
        0.6097248 ,  3.176702  ,  2.1628733 ,  0.61728495,  3.4061713 ,
        0.        ,  0.        ,  0.        ,  0.29591182,  0.        ,
        0.        ,  0.10130256,  1.1335897 ,  1.2777826 ,  0.8302767 ,
        2.6991487 ,  0.38405126,  0.3558884 ,  0.3093865 ,  3.1627026 ,
        0.90818435,  1.5821178 ,  4.476885  ,  0.05102144,  2.3440545 ,
        8.50686   ,  5.4414573 ,  1.9958314 ,  1.2835065 ,  7.4436736 ,
        0.50462204,  1.1515855 ,  3.795001  ,  8.09217   ,  0.1399529 ,
        0.2164765 ,  1.7777822 ,  1.7410293 ,  2.8973055 ,  1.3417593 ,
        2.204526  ,  5.090332  ,  0.1847788 ,  2.0926423 ,  0.0145777 ,
        2.3543062 ,  5.509358  ,  1.9695319 ,  0.18886425,  1.077429  ,
        9.415661  , 15.889854  , 12.685659  ,  1.0936186 ,  0.08539726,
        4.006612  ,  4.256728  ,  0.        ,  0.21611269,  4.7762384 ,
        9.66073   ,  9.821564  ,  4.8410144 ,  7.7786994 ,  4.7317953 ,
       14.324765  ,  7.96984   ,  5.6393456 ,  5.578972  , 13.130465  ,
       13.927779  ,  2.4484336 ,  0.84697866,  5.306067  , 11.231367  ,
        0.9083762 ,  4.578964  ,  7.584468  ,  1.6068283 ,  0.9421862 ,
        0.57203454,  4.5680537 ,  1.8110919 ,  2.1486418 ,  1.6363107 ,
        8.78365   ,  8.156862  ,  2.054801  ,  4.308779  , 11.444415  ,
        6.397045  ,  4.1292677 ,  1.548452  , 10.04043   ,  9.031294  ,
        4.991867  ,  5.779587  ,  5.6803293 ,  4.176216  ,  1.3663089 ,
        0.61768955,  0.24463785,  0.60292834,  1.8037583 ,  1.1593006 ,
        1.493993  ,  0.14449571,  0.72902644,  0.000655  ,  6.8144875 ,
        3.2211418 ,  0.74021226,  0.17808329,  0.69551677,  1.1112485 ,
        0.10865157,  1.810338  ,  7.303304  ,  2.7796025 ,  5.057292  ,
        0.7856973 ,  1.9107257 ,  0.9573493 ,  0.06284843,  0.        ,
        0.13056447,  0.        ,  0.6781369 ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.0069811 ,  0.05219022,
        0.        ,  0.        ,  0.        ,  0.95004684,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  1.4526907 ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.17995411,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.00332065,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  3.4403627 ,
        2.371839  ,  0.39355543,  4.629946  ,  0.4920092 ,  0.        ,
        0.02409126,  0.        ,  0.01973301,  0.        ,  0.        ,
        0.14865024,  0.16587724,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.00871015,  0.        ,  0.        ,
        0.        ,  0.00696385,  0.        ,  0.        ,  1.0388283 ,
        3.2849278 ,  2.6738229 ,  0.7287781 ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.54970086,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.13205789,  0.        ,  0.        ,  0.        ,  0.8668772 ,
        1.4272355 ,  6.583727  ,  2.9902425 ,  0.2383043 ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.1143294 ,
        0.        ,  0.16461715,  1.5917548 , 27.02136   ,  0.        ,
       15.584168  ,  3.0962813 ,  0.06765965,  0.        ,  0.        ,
        0.        ,  0.12260323,  0.        ,  1.7121929 ,  4.85047   ,
        2.6838531 ,  2.5217037 ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        , 19.55956   ,  3.2848659 ,  5.8543296 ,
        4.4314227 ,  0.5629569 ,  1.9576589 ,  6.21776   ,  2.6271045 ,
        2.4235353 ,  2.9017496 ,  0.8701438 ,  5.8177104 ,  2.4560542 ,
        5.0103784 ,  1.0420306 ,  0.4262568 ,  1.4804789 ,  2.7795043 ,
        0.1289667 ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.5629367 ,  3.390016  ,
        0.8993299 ,  0.        ,  0.        ,  0.10453234,  3.571415  ,
        1.1524334 ,  0.33238125,  0.71739197,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.32358602,  0.        ,  1.2422369 ,  0.37855643,
        0.26125684,  1.6899167 ,  2.811209  ,  0.3833846 ,  0.        ,
        0.41985893,  0.2368296 ,  0.8052065 ,  0.9639675 ,  0.867919  ,
       10.252362  ,  3.9603522 ,  8.1239    ,  0.433884  ,  2.0344129 ,
        4.5832624 ,  5.2479897 ,  9.553278  ,  3.6337192 ,  5.572575  ,
        4.087827  ,  0.7920468 ,  7.9510574 , 11.125514  ,  4.936119  ,
        5.578837  ,  0.9654217 ,  1.1364019 , 15.808572  , 12.206754  ,
        0.86529094, 12.824273  , 10.09315   , 12.551981  ,  2.0245855 ,
        0.82636076, 22.90645   ,  1.7762122 ,  0.51405114, 17.041683  ,
        7.682241  ,  7.893931  ,  2.445339  ,  5.7840924 , 17.104992  ,
        4.749784  , 10.638633  ,  9.201806  ,  0.        , 19.931896  ,
       13.804424  ,  9.8392105 ,  3.979795  ,  0.6338869 ,  5.5611124 ,
        3.7393482 , 13.914742  ,  8.635159  ,  3.9112465 , 15.883176  ,
        6.7201557 ,  1.7442094 ,  3.6897418 ,  1.8830901 , 11.462723  ,
        6.831369  ,  9.155698  ,  6.284542  ,  7.32334   ,  2.3959725 ,
        0.33928865,  0.37068   ,  1.7256726 ,  5.4435105 ,  0.50095475,
        0.58377177,  3.189042  , 10.773691  , 12.1475    ,  5.978309  ,
       10.516581  ,  9.887717  ,  0.33856553,  7.616873  ,  1.3539697 ,
       10.254058  ,  0.37409464,  3.4047763 ,  5.3735056 ,  3.0830169 ,
        0.3495214 ,  1.4025049 ,  1.4671408 ,  2.411119  ,  0.4033454 ,
        6.761158  ,  4.030739  ,  8.632412  ,  6.6394176 ,  0.92429894,
        1.9818519 ,  4.3254814 ,  8.160402  ,  3.1350052 ,  1.5976515 ,
        3.1103148 ,  0.        ,  0.30156803,  4.2896376 ,  3.434969  ,
        1.7682261 ,  1.6693491 ,  0.8195819 ,  0.7524828 ,  1.5252048 ,
        0.67267156,  1.2184744 ,  3.8741508 ,  5.1671586 ,  0.33788976,
        0.00168577,  0.34652662,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  1.4294376 ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.1618101 ,  0.        ,  0.        ,  0.        ,  0.19665504,
        0.07919554,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        , 16.066444  ,  0.        ,  0.        ,
        0.00040653,  0.        ,  0.        ,  0.        ,  0.55657774,
       10.619227  ,  0.8379515 ,  0.6358483 ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        1.1030996 ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.21650721,  0.23567843,  0.67594594, 11.6523905 ,
        0.        ,  0.22491072,  0.0010414 ,  2.3483713 ,  1.9371929 ,
        1.553942  ,  0.04228101,  6.9548335 ,  0.        ,  0.05628643,
        0.        ,  0.        ,  0.        ,  0.01571763,  3.5045137 ,
        1.1020757 ,  1.2870854 ,  1.8843307 ,  0.55561566,  0.01492587,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.00448852,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  1.8253791 ,
        0.        ,  0.42356864,  2.8833573 ,  1.2674232 ,  0.        ,
        0.        ,  0.07712214,  0.03274654,  0.        ,  0.        ,
        1.439739  ,  1.5356015 , 12.615751  ,  0.30402642,  2.6724024 ,
        1.0352613 ,  0.        ,  2.4746385 ,  0.        ,  0.06637466,
        0.06604248,  1.0538486 ,  0.8384015 ,  2.6205952 ,  0.01244694,
        7.2834735 ,  0.29626122,  0.        ,  0.07797466,  0.11830796,
       23.931288  ,  4.2410703 ,  5.627712  ,  9.848227  ,  2.3619306 ,
        0.71900934, 13.53106   ,  6.273913  ,  1.8271298 ,  5.6775455 ,
       16.816433  ,  5.8906536 ,  0.6348442 ,  2.695535  ,  1.108697  ,
        0.3136709 ,  3.4187658 ,  0.00578216,  0.        ,  0.        ,
        0.27620634,  0.        ,  0.        ,  0.        ,  0.        ,
        0.18043807,  0.822252  ,  0.03608499,  3.5707026 ,  3.8982246 ,
        2.0636559 ,  1.2453268 ,  0.30950516,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.1713508 ,  0.23690431,  0.04962792,
        0.7071111 ,  0.81165946,  1.7329919 ,  0.        ,  0.        ,
        0.02757528,  0.55996984,  0.8094195 ,  1.9193687 ,  0.77849627,
        1.331457  ,  4.4174604 ,  4.754182  ,  4.354914  ,  0.4959446 ,
        1.2181901 ,  1.4238157 ,  3.3338783 ,  4.1657667 ,  1.5717821 ,
        9.667932  ,  2.592115  ,  3.8828998 ,  3.7179759 ,  0.03359056,
        2.4650826 ,  0.9903587 ,  3.4031432 , 16.761044  , 10.882872  ,
        2.372886  ,  1.0980307 ,  6.5878267 , 12.765206  ,  3.4856193 ,
        6.7711987 ,  4.030517  ,  3.57429   ,  5.6411495 ,  1.483279  ,
        0.53214663,  0.4189065 ,  2.363742  ,  2.9583704 ,  0.93881834,
        6.1526513 , 13.766706  ,  1.8001821 ,  3.7300947 ,  6.8840637 ,
        5.870577  ,  6.7737517 ,  2.3960652 ,  3.940956  ,  3.5343401 ,
        3.7842364 ,  9.422354  ,  6.4148035 ,  1.7782235 ,  1.6213937 ,
        3.9695094 ,  2.803879  ,  3.8084645 ,  1.700168  ,  1.7640694 ,
        3.4466906 ,  8.128755  ,  7.324597  ,  3.0418057 ,  4.465253  ,
        5.945008  ,  1.2403934 , 10.673851  ,  4.3200793 ,  4.1807046 ,
        5.5628777 ,  3.057058  ,  6.241708  ,  0.6530128 ,  0.37585962,
        1.401638  ,  2.493164  ,  0.19764805,  4.639569  ,  3.7018304 ,
        5.87538   ,  0.79281694,  0.        ,  1.0054373 ,  6.4406815 ,
        1.1846893 ,  1.7880019 ,  0.31253377,  2.0612319 ,  3.1343231 ,
        2.0579078 ,  0.75272876,  1.912914  ,  0.9665925 ,  1.1602447 ,
        1.3218747 ,  0.9340148 ,  0.54015464,  0.85225004,  0.22625257,
        2.2894418 ,  1.7365354 ,  4.226911  ,  1.1775376 ,  0.96498495,
        1.2864367 ,  2.7021801 ,  0.7922479 ,  1.2044998 ,  0.44636634,
        0.5161565 ,  0.35790196,  0.38936505,  0.38251063,  1.626637  ,
        0.54531354,  0.        ,  0.9318998 ,  0.        ,  0.50947714,
        0.12070328,  0.1283268 ,  2.9250953 ,  1.308689  ,  0.34650952,
        4.402626  ,  0.48209882,  0.6139164 ,  1.9568491 ,  0.        ,
        0.29906863,  0.16987883,  0.09579603,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.13029286,  0.        ,  0.20587985,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.15489578,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.2552221 ,  0.12695578,  0.10042991,  0.00686576,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.06907884,  0.        ,  0.        ,  0.        ,
        0.        ,  0.00165216,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.21126945,  5.749138  ,
        5.4374275 ,  3.3610737 ,  0.00103077,  0.08556359,  0.07880804,
        2.277596  ,  0.11416379,  0.        ,  0.        ,  0.        ,
        0.        ,  4.0256405 ,  1.322553  ,  0.        ,  0.2692001 ,
        0.        ,  0.        ,  1.7372526 ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.45122755,  0.05431353,  0.33383146,  0.6377049 ,
        6.4067054
    ]
    # fmt: on
    precip = xr.DataArray(values, dims=["T"], coords={"T": t}).rename("precip")
    return precip
