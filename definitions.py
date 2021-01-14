import numpy as np

# log norm distribution with 1 peak
def log_norm_func1(data,center1,sigma1,scale1):
    return scale1*(1/(data*np.sqrt(2*np.pi*sigma1**2))*np.exp(-(((np.log(data)-center1)**2)/(2*sigma1**2))))

# log norm distribution with 2 peak
def log_norm_func2(data,center1,sigma1,scale1, center2,sigma2,scale2):
    return scale1*(1/(data*sigma1*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center1)**2)/(2*sigma1**2)))) +\
            scale2*(1/(data*sigma2*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center2)**2)/(2*sigma2**2))))

# log norm distribution with 3 peak
def log_norm_func3(data,center1,sigma1,scale1, center2,sigma2,scale2, center3,sigma3,scale3):
    return scale1*(1/(data*sigma1*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center1)**2)/(2*sigma1**2)))) +\
            scale2*(1/(data*sigma2*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center2)**2)/(2*sigma2**2)))) +\
            scale3*(1/(data*sigma3*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center3)**2)/(2*sigma3**2))))

#log norm distribution with 4 peaks
def log_norm_func4(data,center1,sigma1,scale1, center2,sigma2,scale2, center3,sigma3,scale3, center4,sigma4,scale4):
    return scale1*(1/(data*sigma1*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center1)**2)/(2*sigma1**2)))) +\
            scale2*(1/(data*sigma2*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center2)**2)/(2*sigma2**2)))) +\
            scale3*(1/(data*sigma3*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center3)**2)/(2*sigma3**2)))) +\
            scale4*(1/(data*sigma4*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center4)**2)/(2*sigma4**2))))

#log norm distribution with 5 peaks
def log_norm_func5(data,center1,sigma1,scale1, center2,sigma2,scale2, center3,sigma3,scale3, center4,sigma4,scale4, center5,sigma5,scale5):
    return scale1*(1/(data*sigma1*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center1)**2)/(2*sigma1**2)))) +\
            scale2*(1/(data*sigma2*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center2)**2)/(2*sigma2**2)))) +\
            scale3*(1/(data*sigma3*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center3)**2)/(2*sigma3**2)))) +\
            scale4*(1/(data*sigma4*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center4)**2)/(2*sigma4**2)))) +\
            scale5*(1/(data*sigma5*np.sqrt(2*np.pi))*np.exp(-(((np.log(data)-center5)**2)/(2*sigma5**2))))
