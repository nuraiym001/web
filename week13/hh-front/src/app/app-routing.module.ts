import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompaniesComponent } from "./companies/companies.component";
import { VacanciesComponent } from "./vacancies/vacancies.component";

const routes: Routes = [
  { path: '', redirectTo: '/companies', pathMatch: 'full' },
  { path: 'companies', component: CompaniesComponent },
  { path: 'companies/:companyId/vacancies', component: VacanciesComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
