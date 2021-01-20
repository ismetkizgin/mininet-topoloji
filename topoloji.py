from mininet.topo import Topo
#from functools import partial

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add switches
        R1 = self.addSwitch( 'R1' )
        R2 = self.addSwitch( 'R2' )
        R3 = self.addSwitch( 'R3' )
        R4 = self.addSwitch( 'R4' )
        R5 = self.addSwitch( 'R5' )
        R6 = self.addSwitch( 'R6' )
        R7 = self.addSwitch( 'R7' )
        R8 = self.addSwitch( 'R8' )
        R9 = self.addSwitch( 'R9' )
        R10 = self.addSwitch( 'R10' )

        SW1=self.addSwitch( 'SW1' )
        SW2=self.addSwitch( 'SW2' )
        SW3=self.addSwitch( 'SW3' )
        SW4=self.addSwitch( 'SW4' )
   
        
        

        # Add links


        self.addLink( SW1, SW2 )
        self.addLink( SW1, SW2 )
        self.addLink( SW1, SW2 )

        self.addLink( SW2, SW3 )
        self.addLink( SW2, SW3 )

        self.addLink( SW2, SW4 )
        self.addLink( SW2, SW4 )

        self.addLink( SW4, SW3 )
        self.addLink( SW4, SW3 )

        self.addLink( SW4, SW1 )
        self.addLink( SW4, SW1 )

        self.addLink( SW3, SW1 )
        self.addLink( SW3, SW1 )


        self.addLink( R1, SW1 )
        self.addLink( R1, SW2 )

        self.addLink( R2, SW1 )
        self.addLink( R2, SW2 )

        self.addLink( R3, SW1 )
        self.addLink( R3, SW2 )

        self.addLink( R4, SW1 )
        self.addLink( R4, SW2 )

        self.addLink( R5, SW1 )
        self.addLink( R5, SW2 )

        self.addLink( R6, SW1 )
        self.addLink( R6, SW2 )

        self.addLink( R7, SW1 )
        self.addLink( R7, SW2 )

        self.addLink( R8, SW1 )
        self.addLink( R8, SW3 )

        self.addLink( R9, SW1 )
        self.addLink( R9, SW3 )

        self.addLink( R10, SW1 )
        self.addLink( R10, SW4 )
        
        


topos = { 'mytopo': ( lambda: MyTopo() ) }
#net = Mininet( topo=topo, controller=partial(RemoteController, ip='192.168.1.247', port=6653))