import os
from tools import Coupling


networks = [('DIV66','\t'), ('Random',' ')]

for each in networks:
    c = Coupling(each[0]+'.txt', delimiter=each[1], coupling_enhance_factor=1)
    c_calc = c.calculate
    c_plot = c.plot

    print('\n> Displaying details for network \'{}\' <\n'.format(each[0]))

    c_plot.AverageSynapticWeight_ExcitatoryIncomingLinks(show_norm=True)
    c_plot.AverageSynapticWeight_InhibitoryIncomingLinks(show_norm=True)
    c_plot.AverageSynapticWeight_OutgoingLinks(show_norm=True)

    connection_probability = c_calc.ConnectionProbability()
    synaptic_weight_bound = c_calc.SynapticWeightBounds()
    synaptic_weight_stat = c_calc.SynapticWeight_Stat()
    pos_link_stat = c_calc.PositiveSynapticWeight_Stat()
    neg_link_stat = c_calc.NegativeSynapticWeight_Stat()

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), each[0]+'_stat.txt'), 'w') as fp:
        fp.write('### Statistics of Network \'{}\' ###\n\n'.format(each[0]))
        fp.write('Connection probability: {}\n'.format(connection_probability))
        fp.write('\nStatistics of synaptic weights:\n')
        fp.write('Minimum weight:\t{}\nMaximum weight:\t{}\n'.format(synaptic_weight_bound[0], synaptic_weight_bound[1]))
        fp.write('Mean (all links):\t{}\n'.format(synaptic_weight_stat[0]))
        fp.write('S.D. (all links):\t{}\n'.format(synaptic_weight_stat[1]))
        fp.write('Mean (negative links):\t{}\n'.format(neg_link_stat[0]))
        fp.write('S.D. (negative links):\t{}\n'.format(neg_link_stat[1]))
        fp.write('Mean (positive links):\t{}\n'.format(pos_link_stat[0]))
        fp.write('S.D. (positive links):\t{}'.format(pos_link_stat[1]))

    print('\n------------------------------next------------------------------')
