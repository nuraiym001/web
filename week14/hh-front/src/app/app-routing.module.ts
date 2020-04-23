import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompanyComponent} from './companies/companies.component';
import {VacanciesComponent} from './vacancies/vacancies.component';

const routes: Routes = [
  { path: '', component: CompanyComponent },
  { path: 'companies/:id/vacancies', component: VacanciesComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
