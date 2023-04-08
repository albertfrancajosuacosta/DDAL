import sys



class DDAL():
    """
    A Drift Detection Method Based on Active Learning.
    
    DDAL is a concept drift detection method based on  
    density variation of the most significant instances selected for Active Learning.
    
    More information:
        https://ieeexplore.ieee.org/document/8489364
        
        Albert França Josuá Costa
        Regis Antonio Saraiva Albuquerque
        Eulanda Miranda dos Santos
    """
    
    def __init__(self, size_batch, theta: float = 0.95, lambida: float = 0.95):
        self.theta = theta
        self.lambida = lambida
        self.max_density = sys.float_info.min
        self.min_density = sys.float_info.max
        self.current_density = 0.0
        self.count_selected_instances = 0
        self.size_batch = size_batch
        
    
    def fixed_uncertainty(self,maximum_posteriori):
        selected = False
        if maximum_posteriori < self.lambida:
            selected = True
        return selected
        
    def count_selected_instances(self,maximum_posteriori):
       s = self.fixed_uncertainty(maximum_posteriori)
       if s:
           self.count_selected_instances+=1
    
    
    def compute_current_density(self):
        self.current_density = (float) (self.count_selected_instances/self.size_batch)
        
            
        
        
 
    
    def reset(self, theta: float = 0.95, lambida: float = 0.95):
        self.theta = theta
        self.lambida = lambida
        self.max_density = sys.float_info.min
        self.min_density = sys.float_info.max
        self.current_density = 0.0
        self.count_selected_instances = 0