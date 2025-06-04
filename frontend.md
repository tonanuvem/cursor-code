# Configuração do Frontend com React Admin

## Criação do Projeto

```bash
yarn create vite clientes_admin --template react
cd clientes_admin
yarn
yarn add react-admin ra-data-simple-rest @mui/material @emotion/react @emotion/styled
```

## Código do Frontend

Primeiro, atualize o arquivo `src/main.jsx` (note que no Vite é .jsx ao invés de .js):

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

Substitua o conteúdo do arquivo `src/App.jsx`:

```jsx
import { Admin, Resource } from 'react-admin';
import simpleRestProvider from 'ra-data-simple-rest';
import { ClienteList, ClienteEdit, ClienteCreate } from './components/Clientes';

const dataProvider = simpleRestProvider('http://localhost:8000');

const App = () => (
  <Admin dataProvider={dataProvider}>
    <Resource 
      name="clientes" 
      list={ClienteList} 
      edit={ClienteEdit} 
      create={ClienteCreate}
    />
  </Admin>
);

export default App;
```

Crie o arquivo `src/components/Clientes.jsx`:

```jsx
import {
  List,
  Datagrid,
  TextField,
  Edit,
  Create,
  SimpleForm,
  TextInput,
  EditButton,
  DeleteButton
} from 'react-admin';

export const ClienteList = () => (
  <List>
    <Datagrid>
      <TextField source="id" />
      <TextField source="fname" label="Nome" />
      <TextField source="lname" label="Sobrenome" />
      <TextField source="timestamp" label="Última Atualização" />
      <EditButton />
      <DeleteButton />
    </Datagrid>
  </List>
);

export const ClienteEdit = () => (
  <Edit>
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput source="fname" label="Nome" />
      <TextInput source="lname" label="Sobrenome" />
      <TextInput disabled source="timestamp" label="Última Atualização" />
    </SimpleForm>
  </Edit>
);

export const ClienteCreate = () => (
  <Create>
    <SimpleForm>
      <TextInput source="fname" label="Nome" />
      <TextInput source="lname" label="Sobrenome" />
    </SimpleForm>
  </Create>
);
```

## Executando o Frontend

```bash
yarn dev
```

O frontend estará disponível em `http://localhost:5173` (porta padrão do Vite)

## Características Implementadas

1. Lista de clientes com paginação
2. Ordenação por qualquer campo
3. Filtro de busca global
4. Formulários de criação e edição
5. Exclusão de registros
6. Interface responsiva

## Observações

1. Certifique-se de que a API (backend) está rodando em `http://localhost:8000`
2. O CORS está configurado para aceitar requisições do frontend
3. Os campos são exibidos em português
4. A interface segue o Material Design
5. Vite oferece um desenvolvimento mais rápido que Create React App
6. Hot Module Replacement (HMR) está habilitado por padrão

## Dicas de Desenvolvimento

1. O Vite usa ES modules por padrão, oferecendo melhor performance
2. A porta 5173 é a padrão do Vite, diferente da 3000 do Create React App
3. O hot reload é significativamente mais rápido que no Create React App
4. Os arquivos usam a extensão .jsx ao invés de .js para melhor suporte do Vite 
