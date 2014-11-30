import matplotlib
#matplotlib.use('Agg')
from pylab import *
import ellipse_evolution_odeint as el_od
import sys, getopt

def invariant(solut):
    term1 = 0.5 * (solut[:,3] * solut[:,0] - solut[:,1] * solut[:,2])**2
    term2 = 2 * (solut[:,0] / solut[:,2] + solut[:,2] / solut[:,0])
    return [term1, term2, term1 + term2] 

def main(lambx0_l=[2,3], time_f=50, partlamb_lim=2.2):
    
    time = np.linspace(0.0,time_f,time_f*2+1)
    solut = {}     
    #solving differential equations up  for lambda_{x0} from the list - lambx0_l
    for lambx0 in lambx0_l:
        solut[str(lambx0)] = el_od.eq_solver(lambx0, time)
    
    #plotting the relation.......
    fig = plt.figure(1, figsize = (8.,5))
    ax = plt.subplot(1,1,1)
    #plotting the LHS of eq. 14 for lambda_{x0} = 2 and 3
    plt.plot(time, invariant(solut["2"])[2], "g",
             time, invariant(solut["3"])[2], "b")
    plt.plot(time, invariant(solut["2"])[0], "g-.",
             time, invariant(solut["3"])[0], "b-.")
    plt.plot(time, invariant(solut["2"])[1], "g--",
             time, invariant(solut["3"])[1], "b--")


    #plotting the RHS of eq. 14 for lambda_{x0} = 2 and 3  
    #plt.plot(time[::2], 4 * (1./2 - 1./solut["2"][::2,2]/solut["2"][::2,0]), "go",
     #        time[::2], 4 * (1./3 - 1./solut["3"][::2,2]/solut["3"][::2,0]), "bo")
    plt.xlabel("time", fontsize=16)
    plt.ylabel(r'$1/2 * (\dot{\lambda_x} \lambda_y - \dot{\lambda_y} \lambda_x)^2$,  $2 * (\lambda_x / \lambda_y + \lambda_y / \lambda_x)$', fontsize=16)
    for item in plt.xticks()[1] + plt.yticks()[1]:
        item.set_fontsize(15)
    #ax.set_ylim(0, partlamb_lim)
    #ax.set_xlim(0, time_f)
    plt.tight_layout()
    plt.savefig("ermakov_inv.pdf")
    plt.show()

# the code can be called with the following options
if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "t:",
                               ["time_f="])
    arg_dic = {}
    for opt, arg in opts:
        if opt in ("-t", "--time_f"):
            arg_dic["time_f"] = float(arg)
        
    # calling the main function with command-line arguments (if any defined)  
    main(**arg_dic) 
