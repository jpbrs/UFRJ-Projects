//
//  Servico.swift
//  ijudaApp
//
//  Created by Student on 18/10/19.
//  Copyright © 2019 Student. All rights reserved.
//

import Foundation

class Servico{
    
    let nomeServico: String
    let telefoneServico: String
    
    init(nomeServico: String, telefoneServico: String){
        
        self.nomeServico = nomeServico
        self.telefoneServico = telefoneServico
    }
    
}

class ServicoLista{
    
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
