--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5
-- Dumped by pg_dump version 14.5

-- Started on 2022-11-30 11:58:51

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 210 (class 1259 OID 17187)
-- Name: Authors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Authors" (
    "ISBN" integer NOT NULL,
    "Author Name" character varying NOT NULL
);


ALTER TABLE public."Authors" OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 17180)
-- Name: Book; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Book" (
    "ISBN" integer NOT NULL,
    "Title" character varying NOT NULL,
    "Price" integer NOT NULL,
    "Stock" integer NOT NULL,
    "Total Sales" integer
);


ALTER TABLE public."Book" OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 17194)
-- Name: Genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Genre" (
    "ISBN" integer NOT NULL,
    "Genre" character varying NOT NULL
);


ALTER TABLE public."Genre" OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 17201)
-- Name: Items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Items" (
    "Order Number" integer NOT NULL,
    "ISBN" integer NOT NULL
);


ALTER TABLE public."Items" OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 17206)
-- Name: Orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Orders" (
    "Order Number" integer NOT NULL,
    "Contact Email" character varying NOT NULL,
    "Shipping" character varying(80),
    "Progress" character varying(80)
);


ALTER TABLE public."Orders" OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17242)
-- Name: Publisher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Publisher" (
    "Publisher Email" character varying NOT NULL,
    "Name" character varying NOT NULL,
    "Address" character varying NOT NULL,
    "Phone Number" integer NOT NULL,
    "Banking" character varying NOT NULL
);


ALTER TABLE public."Publisher" OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 17230)
-- Name: Publishes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Publishes" (
    "ISBN" integer NOT NULL,
    "Sales Percentage" integer NOT NULL,
    "Publisher Email" character varying NOT NULL
);


ALTER TABLE public."Publishes" OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 17213)
-- Name: User; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."User" (
    "Email" character varying NOT NULL,
    "Name" character varying NOT NULL,
    "Phone Number" integer NOT NULL,
    "Shipping Info" character varying NOT NULL,
    "Billing Info" character varying NOT NULL
);


ALTER TABLE public."User" OWNER TO postgres;

--
-- TOC entry 3192 (class 2606 OID 17186)
-- Name: Book Book_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Book"
    ADD CONSTRAINT "Book_pkey" PRIMARY KEY ("ISBN");


--
-- TOC entry 3194 (class 2606 OID 17212)
-- Name: Orders Orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Orders"
    ADD CONSTRAINT "Orders_pkey" PRIMARY KEY ("Order Number");


--
-- TOC entry 3200 (class 2606 OID 17248)
-- Name: Publisher Publisher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Publisher"
    ADD CONSTRAINT "Publisher_pkey" PRIMARY KEY ("Publisher Email");


--
-- TOC entry 3196 (class 2606 OID 17219)
-- Name: User User_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY ("Email");


--
-- TOC entry 3198 (class 2606 OID 17250)
-- Name: Publishes isbnPK; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Publishes"
    ADD CONSTRAINT "isbnPK" PRIMARY KEY ("ISBN");


--
-- TOC entry 3202 (class 2606 OID 17220)
-- Name: Orders Orders_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Orders"
    ADD CONSTRAINT "Orders_fk" FOREIGN KEY ("Contact Email") REFERENCES public."User"("Email") NOT VALID;


--
-- TOC entry 3201 (class 2606 OID 17225)
-- Name: Items items_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Items"
    ADD CONSTRAINT items_fk FOREIGN KEY ("ISBN") REFERENCES public."Book"("ISBN") NOT VALID;


-- Completed on 2022-11-30 11:58:51

--
-- PostgreSQL database dump complete
--

