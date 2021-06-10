import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

import {Consulta} from '../models/consulta';
import {Medico} from '../models/medico';
import {Especialidade} from '../models/especialidade';

const API = 'http://localhost:8000/';

@Injectable({
  providedIn: 'root'
})
export class ConsultaService {

  constructor(private httpClient: HttpClient) {}

  listConsultas(): Observable<Consulta[]> {
    return this.httpClient.get<Consulta[]>(API + 'consultas');
  }

  deleteConsulta(id: string){
    this.httpClient.delete(API + 'consultas/' +  id + '/').subscribe();
  }

  getMedico(id: String): Observable<Medico> {
    return this.httpClient.get<Medico>(API + 'medicos/' +  id)
  }

  getEspecialidade(id: String): Observable<Especialidade> {
    return this.httpClient.get<Especialidade>(API + 'especialidades/' + id)
  }

}
