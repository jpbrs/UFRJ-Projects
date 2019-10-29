//
//  NovosContato.swift
//  ijudaApp
//
//  Created by Student on 22/10/19.
//  Copyright © 2019 Student. All rights reserved.
//

import Foundation

class NovoContato{
    
    let nomeNovoContato: String
    let telefoneNovoContato: String
    
    init(nomeNovoContato: String, telefoneNovoContato: String){
        
        self.nomeNovoContato = nomeNovoContato
        self.telefoneNovoContato = telefoneNovoContato
    }
    
}

class NovoContatoLista{
    
    static func getList () -> [Servico]{
        
        return [
            
            Servico(nomeServico:"SAMU", telefoneServico:"192"),
            Servico(nomeServico:"Bombeiros", telefoneServico:"193"),
            Servico(nomeServico:"Policia Militar", telefoneServico:"190"),
            Servico(nomeServico:"Policia Civil", telefoneServico:"197"),
            Servico(nomeServico:"Defesa Civil", telefoneServico:"199")
        ]
        
    }
}
