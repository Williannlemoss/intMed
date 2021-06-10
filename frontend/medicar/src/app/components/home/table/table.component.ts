import {Component, OnChanges, OnInit, SimpleChanges} from '@angular/core';

import {ConsultaService} from '../../../service/consulta.service';
import {ConsultaDTO} from '../../../models/consultaDTO';



@Component({
  selector: 'medicar-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {
  consultasDTO: ConsultaDTO[] = [];
  consultaDto: ConsultaDTO;
  newconsultasDTO: ConsultaDTO[] = [];

  constructor(private consultaService: ConsultaService) {
  }

  ngOnInit() {
    this.consultaService.listConsultas()
      .subscribe(consultas => {
        consultas.map( consulta => {
          this.consultaService.getMedico(consulta.medico).subscribe(medico => {
            this.consultaService.getEspecialidade(medico.especialidade).subscribe(especialidade => {
              this.consultaDto = {
                'idConsulta': consulta.id,
                'especialidade': especialidade.nome,
                'profissional': medico.nome,
                'data': this.convertData(consulta.dia),
                'hora': consulta.horario.substring(0,5)
              }
              console.log(this.consultaDto)
              this.consultasDTO.push(this.consultaDto)
            })
          })
        })
      })
  }

  convertData(dataAmericana: string): string{
    return  dataAmericana.split('-').reverse().join('/');
  }

  deletarConsulta(id: string) {
    this.newconsultasDTO = []
    this.consultasDTO.map(consulta =>{
      if(consulta.idConsulta !== id){
        this.newconsultasDTO.push(consulta);
      }
    });
    this.consultasDTO = this.newconsultasDTO;
    this.consultaService.deleteConsulta(id);
  }

}
